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
suffix = [
    ".jpg",
    ".gif",
    ".png",
    ".jpeg",
    ".bmp"
]

class Meme(commands.Cog):
    @commands.command(help="Show a meme from a subreddit")
    async def showmeme(self, ctx, sub_name="dankmemes"):
        sub = reddit.subreddit(sub_name)
        memes = []
        if sub.over18 and not ctx.channel.is_nsfw():
            await ctx.send("NSFW subreddit detected. Please use the nsfw channel and try again")
        else:
            for post in sub.hot(limit=15):
            #Ignore sticky posts
                if post.stickied: continue
            #Only accept images
                if not post.url.endswith(tuple(suffix)): continue
                memes.append(post.url)
            # check if the list has any links
            if memes:
                response = random.choice(memes)
            else:
                response = f"No memes found in the {sub_name} subreddit"
            await ctx.send(response)

    @commands.command(brief="Create your own meme",
                        help="Available meme templates: distracted_bf, confused_cat, drakepost, \
                        modern_problems, two_buttons, smile")
    async def creatememe(self, ctx, meme, top, bottom=None, extra=None):
        creator = imgflip.ImgFlipCreator()
        response = creator.create(meme, top, bottom,extra)
        await ctx.send(response)