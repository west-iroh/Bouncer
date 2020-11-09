import discord
from typing import Callable, List


class GuildSettings:

    def __init__(self, save_data_func: Callable[[], None], guild: discord.Guild, guild_data: dict = None):
        self._save_data_func = save_data_func
        self._guild = guild
        self._welcome_channel = None
        self._welcome_role = None
        self._log_channel = None
        self._exempt_roles = []

        if guild_data is not None:
            welcome_channel_id = guild_data.get("welcome_channel")
            welcome_role_id = guild_data.get("welcome_role")
            log_channel_id = guild_data.get("log_channel")
            exempt_roles_ids = guild_data.get("exempt_roles", [])

            if welcome_channel_id is not None:
                try:
                    self._welcome_channel = self._guild.get_channel(welcome_channel_id)
                except discord.errors.NotFound:
                    pass
            if welcome_role_id is not None:
                try:
                    self._welcome_role = self._guild.get_role(welcome_role_id)
                except discord.errors.NotFound:
                    pass
            if log_channel_id is not None:
                try:
                    self._log_channel = self._guild.get_channel(log_channel_id)
                except discord.errors.NotFound:
                    pass
            for id in exempt_roles_ids:
                try:
                    self._exempt_roles.append(self._guild.get_role(id))
                except discord.errors.NotFound:
                    pass

    @property
    def welcome_channel(self):
        return self._welcome_channel

    @property
    def welcome_role(self):
        return self._welcome_role

    @property
    def log_channel(self):
        return self._log_channel

    @property
    def exempt_roles(self):
        return self._exempt_roles

    @welcome_channel.setter
    def welcome_channel(self, value: discord.TextChannel):
        self._welcome_channel = value
        self._save_data_func()

    @welcome_role.setter
    def welcome_role(self, value: discord.Role):
        self._welcome_role = value
        self._save_data_func()

    @log_channel.setter
    def log_channel(self, value: discord.TextChannel):
        self._log_channel = value
        self._save_data_func()

    @exempt_roles.setter
    def exempt_roles(self, value: List[discord.Role]):
        self._exempt_roles = value
        self._save_data_func()

    def serialized_data_dict(self):
        guild_data = dict()

        guild_data["welcome_channel"] = None if self._welcome_channel is None else self._welcome_channel.id
        guild_data["welcome_role"] = None if self._welcome_role is None else self._welcome_role.id
        guild_data["log_channel"] = None if self._log_channel is None else self._log_channel.id
        guild_data["exempt_roles"] = [r.id for r in self._exempt_roles]

        return guild_data
