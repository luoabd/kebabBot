"""This test file gets responses for various apis"""

import json
import os
from dotenv import load_dotenv
from urllib.request import urlopen
from random import randint

import praw
import wolframalpha
from googletrans import Translator

load_dotenv()

def get_trivia_response():
    with urlopen("https://opentdb.com/api.php?amount=1&category=31&type=multiple") as url:
        data = json.loads(url.read().decode())
        return data['response_code']

def get_wolframalpha_response():
    wa = wolframalpha.Client(os.getenv('WOLFRAM_ALPHA_KEY'))
    result = wa.query("1+1")
    answer = next(result.results).text
    return answer

def get_translate_response():
    translator = Translator()
    return translator.translate('안녕하세요.').text

def get_reddit_response():
    reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'), client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                         user_agent=os.getenv('REDDIT_USER_AGENT'))

    def get_submission(subreddit):
        counter = 0
        submissions = [x for x in reddit.subreddit(subreddit).hot(limit=150) if not x.stickied and x.url]
        limit = randint(0, len(submissions) - 1)
        for sub in submissions:
            if counter == limit:
                return sub
            else:
                counter += 1

    submission = get_submission('showerthoughts')
    showerthought = submission.title
    if submission.selftext is not None:
        showerthought += "\n\n" + submission.selftext
    return showerthought

def get_discord_response():
    with urlopen("https://srhpyqt94yxb.statuspage.io/api/v2/status.json") as url:
        data = json.loads(url.read().decode())
        return data['status']['description'] == 'All Systems Operational'