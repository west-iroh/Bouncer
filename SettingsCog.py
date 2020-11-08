import discord
from discord.ext import commands


class SettingsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    # SET

    @commands.group()
    @commands.guild_only()
    async def set(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid set command passed...')

    @set.command(name="welcome_channel")
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel):
        settings = self.client.settings.get_guild_settings(ctx.guild)
        settings.welcome_channel = channel
        await ctx.send('set welcome_channel to {}'.format(channel))

    @set_welcome_channel.error
    async def set_welcome_channel_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that channel...')

    @set.command(name="log_channel")
    async def set_log_channel(self, ctx, channel: discord.TextChannel):
        settings = self.client.settings.get_guild_settings(ctx.guild)
        settings.log_channel = channel
        await ctx.send('set log_channel to {}'.format(channel))

    @set_log_channel.error
    async def set_log_channel_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that channel...')

    @set.command(name="welcome_role")
    async def set_welcome_role(self, ctx, role: discord.Role):
        settings = self.client.settings.get_guild_settings(ctx.guild)
        settings.welcome_role = role
        await ctx.send('set welcome_role to {}'.format(role))

    @set_welcome_role.error
    async def set_welcome_role_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that role...')

    # GET

    @commands.group()
    @commands.guild_only()
    async def get(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid set command passed...')

    @get.command(name="welcome_channel")
    async def get_welcome_channel(self, ctx):
        settings = self.client.settings.get_guild_settings(ctx.guild)
        await ctx.send('welcome_channel is {}'.format(settings.welcome_channel))

    @get.command(name="log_channel")
    async def get_log_channel(self, ctx):
        settings = self.client.settings.get_guild_settings(ctx.guild)
        await ctx.send('log_channel is {}'.format(settings.log_channel))

    @get.command(name="welcome_role")
    async def get_welcome_role(self, ctx):
        settings = self.client.settings.get_guild_settings(ctx.guild)
        await ctx.send('welcome_role is {}'.format(settings.welcome_role))