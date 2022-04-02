# bot.py
import os
import random

import discord
from dotenv import load_dotenv
#from kahoot import client
from discord.ext import commands
#bot = client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!")

# client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    brooklyn_99_quotes = [
        'kahoot poll!'
    ]

    if message.content.startswith('https://kahoot.it/?pin='):
        response = random.choice(brooklyn_99_quotes)

        # pin_index = message.content.find("pin")
        # ampersand_index = message.content.find("&")
        # if (pin_index != -1) and (ampersand_index != -1):
        #     pin = message.content[pin_index: ampersand_index]
        #     bot.join(pin,"KahootPY")
        #     def joinHandle():
        #         pass
        #     bot.on("joined",joinHandle)

        await message.channel.send(response)
    else:
        pass
    
@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")    
        
bot.run(TOKEN)



