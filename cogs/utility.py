import os
from dotenv import load_dotenv
from discord.ext import commands
from googletrans import Translator
import wolframalpha

load_dotenv()

class Utility(commands.Cog):
    """Utility Bot commands."""
    def __init__(self, bot):
        self.bot = bot
        self.wolfram = wolframalpha.Client(os.getenv('WOLFRAM_ALPHA_KEY'))
        self.translator = Translator()
        self.auto_translation = False

    @commands.command(help="Translate text to a language (default=English)")
    async def translate(self, ctx, text, lang="en"):
        if lang.lower() == "chinese":
            lang = "zh-cn"
        translation = self.translator.translate(text, dest=lang)
        await ctx.send(f'translation: {translation.text}')

    @commands.command(help="Use Wolfram Alpha to answer (almost) any question", aliases = ['question'])
    async def wolfram_alpha(self, ctx, *, query):
        try:
            result = self.wolfram.query(query)
            answer = next(result.results).text
        except Exception as e:
            log.warning('ask: Cannot parse result')
            log.error(e)
            return await ctx.send('Cannot parse result.')
        await ctx.send(answer)
