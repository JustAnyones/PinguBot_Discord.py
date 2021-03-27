from discord.ext import commands

class CommandName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def CommandName(self, ctx):
        return

def setup(client):
    client.add_cog(CommandName(client))
