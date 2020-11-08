import json
import os
import discord
from GuildSettings import GuildSettings


class Settings:

    def __init__(self, client: discord.client, db_file: str):
        self._client = client
        self._db_file = db_file
        self._data = dict()
        self._load()

    def _load(self):
        try:
            f = open(self._db_file, 'r')
        except IOError:
            self._save()
        else:
            with f:
                json_data = json.load(f)
                for guild_id, guild_data in json_data.items():
                    if (guild := self._client.get_guild(int(guild_id))) is not None:
                        self._data[guild] = GuildSettings(self._save, guild, guild_data)

    def _save(self):
        json_data = {}
        for guild, guild_settings in self._data.items():
            json_data[guild.id] = guild_settings.serialized_data_dict()

        with open(self._db_file, 'w+') as f:
            json.dump(json_data, f)

    def add_guild(self, guild: discord.guild):
        self._data[guild] = GuildSettings(self._save, guild)
        self._save()

    def get_guild_settings(self, guild: discord.guild):
        data = self._data.get(guild)
        if data is not None:
            return data
        else:
            self.add_guild(guild)
            return self._data[guild]
