from discord.ext import commands
from googletrans import Translator

class Translate(commands.Cog):
    """Bot commands to help translate messages."""
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()
        self.auto_translation = False

    @commands.command(help="Translate text to a language (default=English)")
    async def translate(self, ctx, text, lang="en"):
        if lang.lower() == "chinese":
            lang = "zh-cn"
        translation = self.translator.translate(text, dest=lang)
        await ctx.send(f'translation: {translation.text}')

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

    # Auto-translate text
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        language = self.translator.detect(message.content.lower())
        if self.auto_translation and not language.lang == "en":
            translation = self.translator.translate(message.content.lower())
            await message.channel.send(f'**{message.author.display_name}** said: {translation.text}')