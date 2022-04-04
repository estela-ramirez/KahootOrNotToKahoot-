import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import kahootscrapper

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='pin')
async def nine_nine(ctx, gamePin, gameName):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
    await ctx.send('your game pin is: ' + gamePin + ' and your player name is ' + gameName)
    # convert pin to int
    gamePin = int(gamePin)
    stepOne = kahootscrapper.setup_game(gamePin, gameName)
    kahootscrapper.make_selection(stepOne)
    
    await ctx.send(response)

bot.run(TOKEN)