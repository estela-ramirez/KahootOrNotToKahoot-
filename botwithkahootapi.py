# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from kahoot import client

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


discord_client = discord.Client()


@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        return

    brooklyn_99_quotes = [
        'kahoot poll api!'
    ]

    if message.content.startswith('https://kahoot.it/?pin='):
        response = random.choice(brooklyn_99_quotes)

        kahoot_bot = client()
        kahoot_bot.join(9928864,"KahootPY")
        def joinHandle():
            pass
        kahoot_bot.on("joined",joinHandle)
        #pin_index = message.content.find("pin")
       # ampersand_index = message.content.find("&")
       # if (pin_index != -1) and (ampersand_index != -1):
        #    pin = message.content[pin_index: ampersand_index]
            

        await message.channel.send(response)
    else:
        pass


        
discord_client.run(TOKEN)



