import tweepy
import sys 

credentials = {
    "api_key": "fGtHIKXOazglrl8K6PaMZxHNf",
    "api_secret": "tKJhQndV6A6J4qPVvMudHGumJnFHEZfC6TZYJBCN7LxgIhKliT",
    "access_token": "1241156834959994884-lYXnv8soPtL5I7Dwj3CXrJxGslNh7K",
    "token_secret": "t8W0aKprfbPrRH7UUiYNOixyyRbZJwe78EVkac0iyJKhA"
}
class twitterBot:
    def __init__(self, credentials):
        self.auth = tweepy.OAuthHandler(credentials["api_key"], credentials["api_secret"])
        self.auth.set_access_token(credentials["access_token"], credentials["token_secret"])
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)
    
    def friend(self, user):
        self.api.create_friendship(user)


bot = twitterBot(credentials)

if sys.argv[1] == "tweet":
    bot.tweet(sys.argv[2])

if sys.argv[1] == "friend":
    bot.friend(sys.argv[2])

