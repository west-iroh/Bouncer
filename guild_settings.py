import discord
from typing import Callable


class GuildSettings:

    def __init__(self, save_data_func: Callable[[], None], guild: discord.Guild, guild_data: dict = None):
        self._save_data_func = save_data_func
        self._guild = guild
        self._welcome_channel = None
        self._welcome_role = None
        self._log_channel = None

        if guild_data is not None:
            welcome_channel_id = guild_data.get("welcome_channel")
            welcome_role_id = guild_data.get("welcome_role")
            log_channel_id = guild_data.get("log_channel")

            if welcome_channel_id is not None:
                self._welcome_channel = self._guild.get_channel(welcome_channel_id)
            if welcome_role_id is not None:
                self._welcome_role = self._guild.get_role(welcome_role_id)
            if log_channel_id is not None:
                self._log_channel = self._guild.get_channel(log_channel_id)

    @property
    def welcome_channel(self):
        return self._welcome_channel

    @property
    def welcome_role(self):
        return self._welcome_role

    @property
    def log_channel(self):
        return self._log_channel

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

    def serialized_data_dict(self):
        guild_data = {}
        if self._welcome_channel is None:
            guild_data["welcome_channel"] = None
        else:
            guild_data["welcome_channel"] = self._welcome_channel.id

        if self._welcome_role is None:
            guild_data["welcome_role"] = None
        else:
            guild_data["welcome_role"] = self._welcome_role.id

        if self._log_channel is None:
            guild_data["log_channel"] = None
        else:
            guild_data["log_channel"] = self._log_channel.id

        return guild_data
