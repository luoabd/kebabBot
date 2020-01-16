from discord.ext import commands
from googletrans import Translator

def readfile(filename):
    with open(filename) as handle:
        output = []
        for line in handle:
            line = line.rstrip()
            output.append(line)
    return output

class Admin(commands.Cog):
    """Bot commands available for Administrators."""
    def __init__(self, bot):
        self.bot = bot
        self.swear_words = readfile("./strings/swear_words.txt")
        self.profanity_warning = False

    @commands.command(help="Turn on/off the profanity warning (default=off)")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def profanity(self, ctx):
        self.profanity_warning = not self.profanity_warning
        if self.profanity_warning:
            await ctx.send('The profanity warning is now **on**')
        else:
            await ctx.send('The profanity warning is now **off**')

    @profanity.error
    async def profanity_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f"You need to be an administrator {ctx.message.author.mention}")
    # Profanity warning
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.profanity_warning and any(word in message.content.lower() for word in self.swear_words):
            await message.channel.send(f'{message.author.mention}, no swearing in this server!')