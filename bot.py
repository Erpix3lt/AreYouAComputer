import praw
import time
import os
from dotenv import load_dotenv
from logger import Logger

load_dotenv()

class RedditBot:
    def __init__(self, is_sleep=True):
        self.reddit = praw.Reddit(
            client_id=os.getenv('CLIENT_ID'),
            client_secret=os.getenv('CLIENT_SECRET'),
            username=os.getenv('USERNAME'),
            password=os.getenv('PASSWORD'),
            user_agent=os.getenv('USER_AGENT')
        )
        self.subreddit_name = "DeadInternetTheory"
        self.comment_text = "Are you a computer?"
        self.is_sleep = is_sleep
        self.logger = Logger()

    def post_comment(self):
        try:
            subreddit = self.reddit.subreddit(self.subreddit_name)
            latest_post = next(subreddit.new(limit=1))
            latest_post.reply(self.comment_text)
            message = f"Comment posted on the latest post (ID: {latest_post.id})"
            print(message)
            self.logger.log_message(message)
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            self.logger.log_message(error_message)

    def run(self):
        self.post_comment()
        if self.is_sleep:
            time.sleep(10)

if __name__ == "__main__":
    bot = RedditBot(
        subreddit_name="bot", 
        comment_text="Hello world! This is a test comment."
    )
    bot.run()
