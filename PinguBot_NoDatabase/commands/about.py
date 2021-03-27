from datetime import datetime
from discord.ext import commands
from discord.embeds import Embed, EmptyEmbed

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
        embed = Embed(
            title='Pingu Bot',
            description='A simple Discord Bot that\'s somewhat useful?',
            colour=0x0099ff,
            url=self.client.config.get('bot website', EmptyEmbed),
            timestamp=datetime.now()
        )

        applicationInfo = await self.client.application_info()
        botOwner = applicationInfo.owner

        embed.set_author(
            name=f'{botOwner.name}#{botOwner.discriminator}',
            icon_url=botOwner.avatar_url_as(static_format='png', size=256),
            url=self.client.config.get('bot owner website', EmptyEmbed)
        )

        botImageUrl = self.client.user.avatar_url_as(static_format='png', size=256)
        embed.set_image(url=botImageUrl)
        embed.set_thumbnail(url=botImageUrl)

        embed.add_field(name='The Best Penguin Around', value='It\'s Pingu your friendly neighborhood Noot!')
        embed.add_field(name='How does it work?', value='Using discord.py', inline=False)
        embed.add_field(name='Who\'s it for?', value='People who like Pingu', inline=False)
        embed.add_field(name='What does it do?', value=f'Check {self.client.prefix}help for that pal.', inline=False)

        # TODO: Ask Ene7 about what should the footer be
        embed.set_footer(
            text=EmptyEmbed,
            icon_url=EmptyEmbed
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
