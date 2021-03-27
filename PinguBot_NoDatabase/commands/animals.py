import json

from discord.embeds import Embed
from discord.ext import commands

from utils import sendGetRequest

class Animals(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bird(self, ctx):
        try:
            responseData = await sendGetRequest('https://some-random-api.ml/img/birb')
            data = json.loads(responseData)

            embed = Embed(
                title='Tweet tweet 🐦',
                colour=0x0099ff
            )
            embed.set_image(url=data['link'])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'Couldn\'t send bird because of: {e}')
            return

    @commands.command()
    async def cat(self, ctx):
        try:
            responseData = await sendGetRequest('https://aws.random.cat/meow')
            data = json.loads(responseData)

            embed = Embed(
                title='Meow 🐱',
                colour=0x0099ff
            )
            embed.set_image(url=data['file'])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'Couldn\'t send cat because of: {e}')
            return

    @commands.command()
    async def dog(self, ctx):
        try:
            responseData = await sendGetRequest('https://dog.ceo/api/breeds/image/random')
            data = json.loads(responseData)

            embed = Embed(
                title='Woof 🐶',
                colour=0x0099ff
            )
            embed.set_image(url=data['message'])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'Couldn\'t send dog because of: {e}')
            return

def setup(client):
    client.add_cog(Animals(client))
