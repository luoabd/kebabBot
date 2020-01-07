import os
from dotenv import load_dotenv
import random

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user.name} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
        )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='joke', help='Responds with a random joke')
async def joke(ctx):
    funny_jokes = [
        'Why are eggs not very much into jokes? Because they could crack up.',
        'You can\'t spell advertisements without semen between the tits.',
        'If my wife made a dollar for every sexist joke I make, she\'d be $0.77 richer right now.'
    ]

    response = random.choice(funny_jokes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice')
async def roll_dice(ctx):
    dice = str(random.choice(range(1, 7)))
    await ctx.send(dice)

bot.run(TOKEN)