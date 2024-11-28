import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents=discord.Intents.default()
intents.members=True
intents.message_content=True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='start', help='Starts a game of Rock, Paper, Scissors, Lizard, Spock')
async def start_game(ctx):
    response = 'Let\'s play Rock, Paper, Scissors, Lizard, Spock! To go first type "first", or to go second type "second". End the game anytime by typing "end".'
    await ctx.send(response)

    def startCheck(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['first', 'second', 'end']
    
    firstChoice = await bot.wait_for('message', check=startCheck)
    if firstChoice.content.lower() == 'end':
        response = 'Game ended.'
        await ctx.send(response)
        return
    
    choices = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']
    while True:
        if firstChoice.content.lower() == 'first':
            response = 'Choose your move: Rock, Paper, Scissors, Lizard, Spock'
            await ctx.send(response)
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in choices+['END']
            playerChoice = await bot.wait_for('message', check=check)
            if playerChoice.content.upper() == 'END':
                response = 'Game ended.'
                await ctx.send(response)
                return
            botChoice = random.choice(choices)
            response = 'I choose '+ botChoice
            await ctx.send(response)
            if playerChoice.content.upper() == botChoice:
                response = 'It\'s a draw!'
                await ctx.send(response)
            elif playerChoice.content.upper() == 'ROCK':
                if botChoice == 'PAPER' or botChoice == 'SPOCK':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'PAPER':
                if botChoice == 'SCISSORS' or botChoice == 'LIZARD':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'SCISSORS':
                if botChoice == 'ROCK' or botChoice == 'SPOCK':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'LIZARD':
                if botChoice == 'ROCK' or botChoice == 'SCISSORS':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'SPOCK':
                if botChoice == 'PAPER' or botChoice == 'LIZARD':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
        elif firstChoice.content.lower() == 'second':
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in choices+['END']
            botChoice = random.choice(choices)
            response = 'I have chose. Now your turn. Choose your move: Rock, Paper, Scissors, Lizard, Spock'
            await ctx.send(response)
            playerChoice = await bot.wait_for('message', check=check)
            if playerChoice.content.upper() == 'END':
                response = 'Game ended.'
                await ctx.send(response)
                return
            response = 'I choose '+ botChoice
            await ctx.send(response)
            if playerChoice.content.upper() == botChoice:
                response = 'It\'s a draw!'
                await ctx.send(response)
            elif playerChoice.content.upper() == 'ROCK':
                if botChoice == 'PAPER' or botChoice == 'SPOCK':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'PAPER':
                if botChoice == 'SCISSORS' or botChoice == 'LIZARD':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'SCISSORS':
                if botChoice == 'ROCK' or botChoice == 'SPOCK':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'LIZARD':
                if botChoice == 'ROCK' or botChoice == 'SCISSORS':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)
            elif playerChoice.content.upper() == 'SPOCK':
                if botChoice == 'PAPER' or botChoice == 'LIZARD':
                    response = 'I win!'
                    await ctx.send(response)
                else:
                    response = 'You win!'
                    await ctx.send(response)

bot.run(TOKEN)