from credentials import *
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_tweets = open('tweets.txt','r')
tweets = my_tweets.readlines()
my_tweets.close()

for tweet in tweets:
    print(tweet)
    if tweet != '\n':
        api.update_status(tweet)
    else:
        pass
    sleep(1800) #posts every half an hour