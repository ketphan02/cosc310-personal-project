import time
from typing import Tuple
import tweepy
from tweepy import OAuthHandler


import os
from dotenv import load_dotenv

root_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(root_path, '.env')
load_dotenv(env_path)

# Authentication
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWITTER_API_KEY_SECRET')

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except Exception:
    print('Failed authentication')


def get_latest_tweet() -> Tuple(str, bool):
    elon_musk_tweets = api.user_timeline(screen_name='elonmusk')

    try:
        elon_musk_latest_tweet = elon_musk_tweets[0]
        return elon_musk_latest_tweet.text, True
    except Exception:
        return 'The request traffic is stuck now, try again!', False
