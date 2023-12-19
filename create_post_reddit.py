import praw
reddit = praw.Reddit(
    client_id = "YOUR_CLIENT_ID", #Unique
    client_secret = "YOUR_CLIENT_SECRET", #Unique
    username="USERNAME",
    password="PASSWORD",
    user_agent = "USER_AGENT_DETAILS"
)
reddit.user.me()
reddit.subreddit("test").submit(
    title = "My firt RedditBot",
    selftext = "This is my first post from a reddit bot"
)
