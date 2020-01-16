import random
from discord.ext import commands

def readfile(filename):
    with open(filename) as handle:
        output = []
        for line in handle:
            line = line.rstrip()
            output.append(line)
    return output

class Fun(commands.Cog):
    """Some fun Bot commands."""
    def __init__(self, bot):
        self.bot = bot
        self.funny_jokes = readfile("./strings/jokes.txt")
        self.confused_images = readfile("./strings/confused.txt")
        self.lewd_images = readfile("./strings/lewd.txt")
        self.pout_images = readfile("./strings/pout.txt")
        self.smug_images = readfile("./strings/smug.txt")
        self.cry_images = readfile("./strings/cry.txt")

    @commands.command(help='Responds with a random joke')
    @commands.guild_only()
    async def joke(self, ctx):
        response = random.choice(self.funny_jokes)
        await ctx.send(response)

    @commands.command(help='Simulates rolling dice')
    async def roll_dice(self, ctx):
        dice = str(random.choice(range(1, 7)))
        await ctx.send(dice)
    @commands.command(help='Shows a picture of anime girl confused')
    async def confused(self, ctx):
        response = random.choice(self.confused_images)
        await ctx.send(response)

    @commands.command(help='Shows a picture of anime girl seeing some lewd stuff')
    async def lewd(self, ctx):
        response = random.choice(self.lewd_images)
        await ctx.send(response)

    @commands.command(help='Shows a picture of anime girl pouting')
    async def pout(self, ctx):
        response = random.choice(self.pout_images)
        await ctx.send(response)

    @commands.command(help='Shows a picture of anime girl being smug')
    async def smug(self, ctx):
        response = random.choice(self.smug_images)
        await ctx.send(response)

    @commands.command(help='Shows a picture of anime girl crying')
    async def cry(self, ctx):
        response = random.choice(self.cry_images)
        await ctx.send(response)