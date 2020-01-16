import os
from dotenv import load_dotenv

from discord.ext import commands
from cogs import music, meme, fun, utility, admin

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

COGS = [music.Music, meme.Meme, fun.Fun, utility.Utility, admin.Admin]
bot = commands.Bot(command_prefix= admin.determine_prefix)

@bot.event
async def on_ready():
    print(
        f'{bot.user.name} is connected to the following server(s):\n'
        f'{bot.guilds}'
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

def run():
    add_cogs(COGS)
    bot.run(TOKEN)