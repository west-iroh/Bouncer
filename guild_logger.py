import discord
from datetime import datetime


class GuildLogger:
    def __init__(self, client: discord.Client, guild: discord.Guild):
        self._client = client
        self._guild = guild

    async def log_ban(self, user: discord.User, age: int):
        embed = discord.Embed(title="Banned User",
                              description= "{} ({} (ID {}))".format(user.mention, user.name, user.id),
                              color=0xff4b4b,
                              timestamp=datetime.now())
        embed.add_field(name="Reason:", value="Underage ({})".format(age), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await self._send_embed(embed)

    async def log_failed_ban(self, user: discord.User, age:int):
        embed = discord.Embed(title="Failed to Ban User",
                              description= "{} ({} (ID {}))".format(user.mention, user.name, user.id),
                              color=0xff00ff,
                              timestamp=datetime.now())
        embed.add_field(name="Reason:", value="Underage ({})".format(age), inline=True)
        embed.add_field(name="Error:", value="Bot does not have permission", inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await self._send_embed(embed)

    async def log_admittance(self, user: discord.User, age: int):
        embed = discord.Embed(title="Admitted User",
                              description="{} ({} (ID {}))".format(user.mention, user.name, user.id),
                              color=0x64ff64,
                              timestamp=datetime.now())
        embed.add_field(name="Age:", value="{}".format(age), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await self._send_embed(embed)

    async def log_failed_admittance(self, user: discord.User, age: int, failed_reason: str):
        embed = discord.Embed(title="Failed to Admit User",
                              description="{} ({} (ID {}))".format(user.mention, user.name, user.id),
                              color=0xff00ff,
                              timestamp=datetime.now())
        embed.add_field(name="Age:", value="{}".format(age), inline=True)
        embed.add_field(name="Error:", value=failed_reason, inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await self._send_embed(embed)

    async def log_disregard(self, user: discord.User, message: str):
        embed = discord.Embed(title="Disregarded Message",
                              description="{} ({} (ID {}))".format(user.mention, user.name, user.id),
                              color=0x969696,
                              timestamp=datetime.now())
        embed.add_field(name="Message:", value="{}".format(message), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await self._send_embed(embed)

    def _get_log_channel(self) -> discord.TextChannel:
        guild_settings = self._client.settings.get_guild_settings(self._guild)
        return guild_settings.log_channel

    async def _send_embed(self, embed: discord.Embed):
        channel = self._get_log_channel()
        try:
            await channel.send(embed=embed)
        except discord.errors.NotFound:
            # channel not found
            pass
        except AttributeError:
            # no channel set
            pass
        except discord.errors.Forbidden:
            # no permission
            pass
