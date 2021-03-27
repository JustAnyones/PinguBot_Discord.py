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

def setup(client):
    client.add_cog(Roll(client))
