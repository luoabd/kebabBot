import os
from dotenv import load_dotenv
import random

from discord.ext import commands
from cogs import music, meme
from googletrans import Translator

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

# global variables
swear_words = readfile("./strings/swear_words.txt")
funny_jokes = readfile("./strings/jokes.txt")
confused_images = readfile("./strings/confused.txt")
lewd_images = readfile("./strings/lewd.txt")
pout_images = readfile("./strings/pout.txt")
smug_images = readfile("./strings/smug.txt")
cry_images = readfile("./strings/cry.txt")
auto_translation = False
profanity_warning = False

COGS = [music.Music, meme.Meme]
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

def add_cogs(COGS):
    for cog in COGS:
        bot.add_cog(cog(bot))

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='joke', help='Responds with a random joke')
@commands.guild_only()
async def joke(ctx):
    response = random.choice(funny_jokes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice')
async def roll_dice(ctx):
    dice = str(random.choice(range(1, 7)))
    await ctx.send(dice)

translator = Translator()
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if profanity_warning and any(word in message.content.lower() for word in swear_words):
        await message.channel.send(f'**{message.author.mention}**, no swearing in this christian server!')
    language = translator.detect(message.content.lower())
    if auto_translation and not language.lang == "en":
        translation = translator.translate(message.content.lower())
        await message.channel.send(f'**{message.author.display_name}** said: {translation.text}')

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

@bot.command(help="Translate text to a language (default=English)")
async def translate(ctx, text, lang="en"):
    if lang.lower() == "chinese":
        lang = "zh-cn"
    translation = translator.translate(text, dest=lang)
    await ctx.send(f'translation: {translation.text}')

@bot.command(help="Turn on/off the profanity warning (default=on)")
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def profanity(ctx):
    global profanity_warning
    profanity_warning = not profanity_warning
    if profanity_warning:
        await ctx.send('The profanity warning is now **on**')
    else:
        await ctx.send('The profanity warning is now **off**')

@profanity.error
async def profanity_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"You need to be an administrator {ctx.message.author.mention}")

@bot.command(help="Turn on/off the auto-translation (default=off)")
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def auto_translate(ctx, error):
    global auto_translation
    auto_translation = not auto_translation
    if auto_translation:
        await ctx.send('The auto translation is now **on**')
    else:
        await ctx.send('The auto translation is now **off**')

@auto_translate.error
async def auto_translate_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"You need to be an administrator {ctx.message.author.mention}")
def run():
    add_cogs(COGS)
    bot.run(TOKEN)