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
        self.translator = Translator()
        self.auto_translation = False
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
        # Auto translate text
        language = self.translator.detect(message.content.lower())
        if self.auto_translation and not language.lang == "en" and not message.content.lower().startswith('$'):
            translation = self.translator.translate(message.content.lower())
            await message.channel.send(f'**{message.author.display_name}** said: {translation.text}')


    @commands.command(help="Turn on/off the auto-translation (default=off)")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def auto_translate(self, ctx):
        self.auto_translation = not self.auto_translation
        if self.auto_translation:
            await ctx.send('The auto translation is now **on**')
        else:
            await ctx.send('The auto translation is now **off**')

    @auto_translate.error
    async def auto_translate_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f"You need to be an administrator {ctx.message.author.mention}")