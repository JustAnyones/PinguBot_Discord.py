import json

from discord.embeds import Embed
from discord.ext import commands

from utils import sendGetRequest

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        try:
            responseData = await sendGetRequest('https://some-random-api.ml/meme')
            data = json.loads(responseData)

            embed = Embed(
                title='Nice Meme',
                colour=0x0099ff
            )
            embed.set_image(url=data['image'])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'Couldn\'t send meme because of: {e}')
            return

def setup(client):
    client.add_cog(Meme(client))
