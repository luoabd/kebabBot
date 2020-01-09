from discord.ext import commands
import discord
import random
import praw
import requests
import json
import imgflip

import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=REDDIT_PASSWORD,
                     user_agent=REDDIT_USER_AGENT,
                     username=REDDIT_USERNAME)

class Meme(commands.Cog):
    @commands.command(help="Show a meme from a subreddit")
    async def showmeme(self, ctx, sub_name="dankmemes"):
        sub = reddit.subreddit(sub_name)
        memes = []
        for post in sub.hot(limit=15):
            if post.stickied: continue
            memes.append(post.url)
        response = random.choice(memes)
        await ctx.send(response)
    @commands.command(brief="Create your own meme",
                        help="Available meme templates: distracted_bf, confused_cat, drakepost, \
                        modern_problems, two_buttons, smile")
    async def creatememe(self, ctx, meme, top, bottom=None, extra=None):
        creator = imgflip.ImgFlipCreator()
        response = creator.create(meme, top, bottom,extra)
        await ctx.send(response)