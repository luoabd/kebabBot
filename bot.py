import os
from dotenv import load_dotenv
import random

from discord.ext import commands
from cogs import music

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

def readfile(filename):
    with open(filename) as handle:
        output = []
        for line in handle:
            line = line.rstrip()
            output.append(line)
    return output

swear_words = readfile("./strings/swear_words.txt")
funny_jokes = readfile("./strings/jokes.txt")
confused_images = readfile("./strings/confused.txt")
lewd_images = readfile("./strings/lewd.txt")
pout_images = readfile("./strings/pout.txt")
smug_images = readfile("./strings/smug.txt")
cry_images = readfile("./strings/cry.txt")

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
    response = random.choice(funny_jokes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice')
async def roll_dice(ctx):
    dice = str(random.choice(range(1, 7)))
    await ctx.send(dice)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if any(word in message.content.lower() for word in swear_words):
        await message.channel.send(f'**{message.author.display_name}**, no swearing in this christian server!')
    await bot.process_commands(message)

@bot.command(name='confused', help='Shows a picture of anime girl confused')
async def confused(ctx):
    response = random.choice(confused_images)
    await ctx.send(response)

@bot.command(name='lewd', help='Shows a picture of anime girl seeing some lewd stuff')
async def lewd(ctx):
    response = random.choice(lewd_images)
    await ctx.send(response)

@bot.command(name='pout', help='Shows a picture of anime girl pouting')
async def pout(ctx):
    response = random.choice(pout_images)
    await ctx.send(response)

@bot.command(name='smug', help='Shows a picture of anime girl being smug')
async def smug(ctx):
    response = random.choice(smug_images)
    await ctx.send(response)

@bot.command(name='cry', help='Shows a picture of anime girl crying')
async def cry(ctx):
    response = random.choice(cry_images)
    await ctx.send(response)

def run():
    # add_cogs(bot)
    bot.add_cog(music.Music(bot))
    bot.run(TOKEN)