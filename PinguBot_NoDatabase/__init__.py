import discord
import json
import os

from discord.ext import commands
from datetime import datetime

# Define some functions for future use
def getTime():
    # That's how American toLocaleTimeString works, I guess

    # 12 hour formatting is platform dependant
    if os.name == 'nt':
        return datetime.now().strftime('%#I:%M:%S %p')
    else:
        return datetime.now().strftime('%-I:%M:%S %p')

def logMessage(guild, channel, username, content):
    print(f'[{getTime()}] {{GUILD: {guild}, CHANNEL: {channel}}} {username} said: {content}')


class PinguBot(commands.Bot):
    def __init__(self, config):
        self.config = config
        self.prefix = self.config.get('prefix', '>')
        super().__init__(command_prefix=self.prefix, help_command=None, case_insensitive=True)

        # Loads commands
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                self.load_extension(f'commands.{filename[:-3]}')


with open('config.json', 'r') as f:
    config = json.load(f)

client = PinguBot(config)

@client.event
async def on_ready():
    print('Pingu Bot is now online!')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name='your calls for help. Say "noot noot" for bot usage.'
        )
    )

@client.event
async def on_message(message):
    authorUsername = f'{message.author.name}#{message.author.discriminator}'
    # Logs every sent message
    logMessage(message.guild, message.channel, authorUsername, message.content)

    # Prevent other bots and this bot form being able to run commands. This prevents command looping!
    if message.author.bot: return

    # Lowers the text for use prematurely
    lowercaseContent = message.content.lower()

    # Handle special events apart from commands
    if 'noot noot' in lowercaseContent or 'hello pingu' in lowercaseContent:
        await message.channel.send(f'<noot emoji here> Noot Noot! Hello {authorUsername}, please use {prefix}help for usage information.')
    elif 'noot' in lowercaseContent:
        await message.reply('<emoji here> noot!')

    if 'sad' in lowercaseContent:
        await message.reply('https://www.youtube.com/watch?v=kGOQfLFzJj8')

    if lowercaseContent == '🐡🐡':
        await message.reply('https://www.youtube.com/watch?v=ckyvBBeMw5w')
    elif '🐡' in lowercaseContent:
        await message.reply('https://www.youtube.com/watch?v=ByILtrrEmwY')

    if '🐢' in lowercaseContent:
        await message.reply('https://www.youtube.com/watch?v=Wl9oUBgFk6Y')

    if 'milk' in lowercaseContent:
        await message.reply('**mmm myes mmilk**', file=discord.File('./images/miau.gif'))

    if 'frog' in lowercaseContent or 'myes' in lowercaseContent:
        await message.reply('**mmm myes pet froge**', file=discord.File('./images/tinyfroge.gif'))

    # Allow bot to process any other commands
    await client.process_commands(message)

# TODO: Handles possible errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        print(error)

client.run(config.get('token', None))
