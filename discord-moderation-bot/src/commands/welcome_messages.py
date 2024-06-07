import discord

class WelcomeMessages:
    def __init__(self, client):
        self.client = client

    async def send_welcome_message(self, member):
        # Customize the welcome message here
        welcome_channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await welcome_channel.send(f"Welcome {member.mention} to the server! Please read the rules in the rules channel.")

    async def on_member_join(self, member):
        await self.send_welcome_message(member)

    async def on_ready(self):
        print("Welcome Messages module loaded.")

def setup(client):
    welcome_messages = WelcomeMessages(client)
    client.add_cog(welcome_messages)