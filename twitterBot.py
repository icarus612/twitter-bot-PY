import tweepy

class TwitterBot:
    def __init__(self, credentials):
        self.auth = tweepy.OAuthHandler(credentials["api_key"], credentials["api_secret"])
        self.auth.set_access_token(credentials["access_token"], credentials["token_secret"])
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)
    
    def friend(self, user):
        self.api.create_friendship(user)