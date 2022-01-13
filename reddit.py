import os
import praw
from dotenv import load_dotenv

load_dotenv('./.env')

print(os.getenv('CLIENT_ID'))

reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    user_agent = os.getenv('USER_AGENT'),
    username = os.getenv('USERNAME'),
    password = os.getenv('PASSWORD')
)

print(reddit.read_only)

subreddit = reddit.subreddit("mexico")

for submission in subreddit.top(limit=10):

    #get submission url
    print(submission.title)
    url = str(submission.url)
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
        print(url)