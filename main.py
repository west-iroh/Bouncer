from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import logging
from Settings import Settings
from SettingsCog import SettingsCog

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


# @client.event
# async def on_message(message):
#     pass
#
#
# @client.event
# async def on_guild_join(guild):
#     client.settings.add_guild(guild)
#
#
# @client.event
# async def on_guild_role_delete(role):
#     pass
#
#
# @client.event
# async def on_guild_channel_delete(channel):
#     pass


client.run(os.getenv('TOKEN'), reconnect=True)
