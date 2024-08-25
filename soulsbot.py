import os
import tweepy
import time
import schedule
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_key = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)