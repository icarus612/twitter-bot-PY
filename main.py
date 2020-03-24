import sys 
from twitterBot import TwitterBot

credentials = {
    "api_key": "fGtHIKXOazglrl8K6PaMZxHNf",
    "api_secret": "tKJhQndV6A6J4qPVvMudHGumJnFHEZfC6TZYJBCN7LxgIhKliT",
    "access_token": "1241156834959994884-lYXnv8soPtL5I7Dwj3CXrJxGslNh7K",
    "token_secret": "t8W0aKprfbPrRH7UUiYNOixyyRbZJwe78EVkac0iyJKhA"
}

bot = TwitterBot(credentials)

if sys.argv[1] == "tweet":
    bot.tweet(sys.argv[2])

if sys.argv[1] == "friend":
    bot.friend(sys.argv[2])