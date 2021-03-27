import discord

from discord.ext import commands
from random import choice

possibleResponses = [
    ('Ooga booga', './images/pingutroll.gif'),
    ('I can\'t read lol', './images/pinguread.gif'),
    ('NOOT NOOT!', './images/pingunoot.gif'),
    ('Spotify premium be like:', './images/pingumusic.gif'),
    ('Meow.', './images/miau.gif'),
    ('Pet **froge**', './images/tinyfroge.gif')
]

class Gif(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx):
        text, filePath = choice(possibleResponses)
        await ctx.send(text, file=discord.File(filePath))

def setup(client):
    client.add_cog(Gif(client))
