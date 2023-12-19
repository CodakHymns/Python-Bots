# TWITTER BOT THAT CAN POST ANYTHONG USING TWITTER API
# Developer: Hymns.py

import tweepy
#API KEYS
consumer_key = "5Xx2Wm2kIOPXoMRMpi1Tt4zKw"
consumer_secret = "pSICn2IAxIhQx72iIsY10ckxe4pMJr2Bn03rgcF3DojiZDAlqB"
access_token = "1475544058521075712-Nwhvu0XPa2VmuiJaq4vqZlAjefWHh7"
access_token_secret = "RkeRDhblUNPpPSWYhlC5Yyo4FXNc3jPm5g8yiCwVdKTyn" 

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Create API object
api = tweepy.API(auth)

#Post
api.update_status('Hello from my twitter Bot')


