import discord

class UserManagement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f'{member.mention} has been muted.')

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'{member.mention} has been warned. Reason: {reason}')

    @commands.command()
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(UserManagement(client))