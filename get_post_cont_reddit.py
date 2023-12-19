#Developer: Hymns.py
#TOPIC: USING PRAW LIBRARY TO INTERACT WITH REDDIT API
#This code retrieves the top 5 most popular posts from the “learnpython” subreddit that are not pinned to the top of the subreddit by a moderator.

import praw

#creating the reddit object withthe provided variables credentials.
reddit = praw.Reddit(
    client_id = "CLIENT_ID", #Unique
    client_secret = "CLIENT_SECRET", #Unique
    user_agent = "myBot/0.0.1"
)

#The line below retrieves authenticated user information by calling the "user.me()" on the reddit object above.
reddit.user.me()
subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit = 5):
    if not submission.stickied:
        print(f'Title: {submission.title}')
        print(f'Score: {submission.score}')
        print(f'Content: {submission.selftext}')
        print("---")
