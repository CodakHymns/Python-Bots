# TWITTER BOT THAT CAN POST ANYTHONG USING TWITTER API
# Developer: Hymns.py

import tweepy
#API KEYS
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET:

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Create API object
api = tweepy.API(auth)

#Post
api.update_status('Hello from my twitter Bot')


