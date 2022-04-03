import tweepy
from tweepy import OAuthHandler


import os
from dotenv import load_dotenv

root_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(root_path, '.env')
load_dotenv(env_path)

consumer_key=os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET')
access_token=os.environ.get('TWITTER_ACCESS_TOKEN')
access_secret=os.environ.get('TWITTER_ACCESS_SECRET')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True)

latest_tweet = api.user_timeline(user_id="elonmusk", count=1)

print(latest_tweet[0].text)

