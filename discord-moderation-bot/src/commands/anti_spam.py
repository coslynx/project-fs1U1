import discord
from discord.ext import commands

class AntiSpam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # Implement anti-spam logic here
        pass

def setup(client):
    client.add_cog(AntiSpam(client))