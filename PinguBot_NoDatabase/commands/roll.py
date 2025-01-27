import discord

from discord.ext import commands
from random import randint

class Roll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx, maxValue: int):
        if maxValue <= 0:
            maxValue = 1
        await ctx.send(f'You rolled a: {randint(1, maxValue)}')

    @commands.command()
    async def roll6(self, ctx):
        rolled = randint(1, 6)
        if rolled == 6:
            await ctx.send(
                'You\'re extra lucky today! Here have some gold coins:',
                file=discord.File('./images/coin_pouch.gif')
            )
        await ctx.send(f'You rolled a: {rolled}')


def setup(client):
    client.add_cog(Roll(client))
