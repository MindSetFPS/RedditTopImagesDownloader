from genericpath import exists
import os
import shutil
import praw
import requests
from dotenv import load_dotenv
import datetime

load_dotenv('./.env')

reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    user_agent = os.getenv('USER_AGENT'),
    username = os.getenv('USERNAME'),
    password = os.getenv('PASSWORD')
)

print(reddit.read_only)

subreddit = reddit.subreddit("mexico")

dir = os.getcwd()
current_week = datetime.datetime.utcnow().isocalendar()[1]
dirpath = os.path.join(dir, 'week' + str(current_week))

if (os.path.isdir(dirpath) == False):
    os.mkdir(dirpath, exist_ok=True)
else:
    print('Directory already exists')

for submission in subreddit.top(limit=3):
    #get submission url
    print(submission.title)
    url = str(submission.url)
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
        filename = str(submission.upvote_ratio)     + '% ' + str(submission.score) + ' upvotes ' + submission.id
        r = requests.get(submission.url, stream = True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open( os.path.join( dirpath, filename ), 'wb') as f:
                shutil.copyfileobj(r.raw,  f)
        # print(submission.url)