import discord

class ReportingSystem:
    def __init__(self, client):
        self.client = client

    async def report_user(self, message, user_id, reason):
        try:
            user = await self.client.fetch_user(user_id)
            report_channel = discord.utils.get(message.guild.text_channels, name='reports')
            
            if report_channel is None:
                overwrites = {
                    message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    message.guild.me: discord.PermissionOverwrite(read_messages=True)
                }
                report_channel = await message.guild.create_text_channel('reports', overwrites=overwrites)

            report_embed = discord.Embed(
                title='User Report',
                description=f'Report against {user.mention}',
                color=discord.Color.red()
            )
            report_embed.add_field(name='Reporter', value=message.author.mention, inline=False)
            report_embed.add_field(name='Reported User', value=user.mention, inline=False)
            report_embed.add_field(name='Reason', value=reason, inline=False)

            await report_channel.send(embed=report_embed)
            await message.channel.send(f'Report against {user.mention} has been submitted successfully.')
        
        except discord.Forbidden:
            await message.channel.send('I do not have the necessary permissions to create the report channel.')
        
        except discord.HTTPException:
            await message.channel.send('An error occurred while processing the report. Please try again later.')

    async def handle_reports(self, message):
        if message.content.startswith('!viewreports'):
            report_channel = discord.utils.get(message.guild.text_channels, name='reports')
            if report_channel is not None:
                async for msg in report_channel.history(limit=10):
                    if msg.author == self.client.user:
                        await message.channel.send(msg.content)
        elif message.content.startswith('!clearreports'):
            report_channel = discord.utils.get(message.guild.text_channels, name='reports')
            if report_channel is not None:
                await report_channel.purge()
                await message.channel.send('Reports have been cleared.')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('!report'):
            user_id, *reason = message.content.split()[1:]
            await self.report_user(message, int(user_id), ' '.join(reason))

        if message.content.startswith('!viewreports') or message.content.startswith('!clearreports'):
            await self.handle_reports(message)