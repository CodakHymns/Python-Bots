import praw
reddit = praw.Reddit(
    client_id = "Bk2_1o8l2c86QepAn655_A", #Unique
    client_secret = "_HAJWURq2MVWgdBsoYSu0hnfhuApCg", #Unique
    username="Hymns_py",
    password="optiplexgx520 ",
    user_agent = "myBot/0.0.2"
)
reddit.user.me()
reddit.subreddit("test").submit(
    title = "My firt RedditBot",
    selftext = "This is my first post from a reddit bot"
)
