# bot.py
import os
import random

import discord
from dotenv import load_dotenv
import webbrowser
#
from urllib.parse import urljoin

from bs4 import BeautifulSoup

import requests
#

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='link')
async def nine_nine(ctx , kahootLink):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    webbrowser.open(kahootLink)
   # https://kahoot.it/join
    crisil_url = 'https://kahoot.it/?pin=' + '9928864' + '&refer_method=link'
    r = requests.post(crisil_url, data="nicks")

    soup = BeautifulSoup(r.content, features="html.parser")

    tags = {tag.name for tag in soup.find_all()}
    results = soup.find_all("nickname")
    class_list = set()  
    # iterate all tags
    for tag in tags:
    
        # find all element of tag
        for i in soup.find_all( tag ):
    
            # if tag has attribute of class
            if i.has_attr( "class" ):
    
                if len( i['class'] ) != 0:
                    class_list.add(" ".join( i['class']))
    
    print( class_list )
    print (results)
    print(tags)
    tag = soup.body
  
    # Get the attribute
    attribute = tag.attrs
    print(attribute)
    body = soup.find('body')
    the_contents_of_body_without_body_tags = body.findChildren(recursive=False)
    print(the_contents_of_body_without_body_tags)
    await ctx.send(response)


bot.run(TOKEN)