# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents=discord.Intents.default()
intents.members=True
intents.message_content=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

author = None
choices= ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']
@client.event
async def on_message(message):
    global author
    if message.author == client.user:
        return
    
    if message.content == '.gb':
        author = message.author
        response = 'Let\'s play Rock, Paper, Scissors, Lizard, Spock! End the game anytime by typing "end". Choose first!'
        await message.channel.send(response)
        return

    if message.author!=author:
        return
    
    if message.content == 'end':
        response = 'Game ended.'
        await message.channel.send(response)
        author = None
        return
    
    choice= random.choice(choices)
    
    if message.content.upper() == choice:
        response= 'I choose '+ choice
        await message.channel.send(response)
        response= 'It\'s a draw!'
        await message.channel.send(response)
    elif message.content.upper() == 'ROCK':
        response= 'I choose '+ choice
        await message.channel.send(response)
        if choice == 'PAPER' or choice == 'SPOCK':
            response= 'I won!'
            await message.channel.send(response)
        else:
            response= 'You won!'
            await message.channel.send(response)
    elif message.content.upper() == 'PAPER':
        response= 'I choose '+ choice
        await message.channel.send(response)
        if choice == 'SCISSORS' or choice == 'LIZARD':
            response= 'I won!'
            await message.channel.send(response)
        else:
            response= 'You won!'
            await message.channel.send(response)
    elif message.content.upper() == 'SCISSORS':
        response= 'I choose '+ choice
        await message.channel.send(response)
        if choice == 'ROCK' or choice == 'SPOCK':
            response= 'I won!'
            await message.channel.send(response)
        else:
            response= 'You won!'
            await message.channel.send(response)
    elif message.content.upper() == 'LIZARD':
        response= 'I choose '+ choice
        await message.channel.send(response)
        if choice == 'ROCK' or choice == 'SCISSORS':
            response= 'I won!'
            await message.channel.send(response)
        else:
            response= 'You won!'
            await message.channel.send(response)
    elif message.content.upper() == 'SPOCK':
        response= 'I choose '+ choice
        await message.channel.send(response)
        if choice == 'PAPER' or choice == 'LIZARD':
            response= 'I won!'
            await message.channel.send(response)
        else:
            response= 'You won!'
            await message.channel.send(response)
    
client.run(TOKEN)