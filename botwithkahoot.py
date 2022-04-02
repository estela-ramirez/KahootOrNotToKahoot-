# bot.py
import os
import json
import asyncio
import random

import discord
from dotenv import load_dotenv
from kahoot import client as account
from discord.ext import commands
#bot = client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!")

thing = account()

# client = discord.Client()

# @bot.command()
# async def ping(ctx):
# 	await ctx.channel.send("pong")  

@bot.command()
async def join(ctx, arg):
    thing.join(arg, f"KahootPY")
    def joinHandle():
         pass
    thing.on("joined", joinHandle()
    await ctx.send("Bot deployed") 

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
  
bot.run(TOKEN)



