from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import logging
from settings import Settings
from settings_cog import SettingsCog
from guild_logger import GuildLogger

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv('.env')

intents = discord.Intents.default()
intents.typing = False
intents.reactions = False
intents.voice_states = False
intents.invites = False
intents.webhooks = False
intents.integrations = False

client = commands.Bot(intents=intents, command_prefix="/bouncer ")

client.add_cog(SettingsCog(client))


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    client.settings = Settings(client, "db.json")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms ')


@client.check
async def global_command_check(ctx):
    if ctx.author.bot:
        return False
    if ctx.guild is None:
        return True
    else:
        return ctx.guild.owner_id == ctx.author.id or ctx.author.guild_permissions.administrator


@client.listen('on_message')
async def handle_message(message):
    if message.guild is None or message.author.bot:
        return
    settings = client.settings.get_guild_settings(message.guild)
    if settings.welcome_channel == message.channel:
        guild_logger = GuildLogger(client, message.guild)
        try:
            age = int(message.content)
        except ValueError:
            await guild_logger.log_disregard(message.author, message.content)
        else:
            if 18 <= age <= 120:
                try:
                    await message.author.add_roles(settings.welcome_role)
                except discord.errors.NotFound:
                    await guild_logger.log_failed_admittance(message.author,
                                                             age,
                                                             "No welcome_role has been set")
                except AttributeError:
                    await guild_logger.log_failed_admittance(message.author,
                                                             age,
                                                             "No welcome_role has been set")
                except discord.errors.Forbidden:
                    await guild_logger.log_failed_admittance(message.author,
                                                             age,
                                                             "Bot does not have permission to give role")
                else:
                    await guild_logger.log_admittance(message.author, age)
            else:
                try:
                    await message.author.ban(reason="Banned for being underage ({})".format(age))
                except discord.errors.Forbidden:
                    await guild_logger.log_failed_ban(message.author, age)
        try:
            await message.delete()
        except discord.errors.Forbidden:
            # no permission to delete message
            pass

client.run(os.getenv('TOKEN'), reconnect=True)
