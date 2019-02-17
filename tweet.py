"""
This program calls the home_timeline API method to retrieve the 20 most recent tweets from your timeline.

Helpfull Link: http://docs.tweepy.org/en/v3.5.0/api.html#id1

"""
from __future__ import print_function
import tweepy
from emoji import emojize


print("=" * 20, "\033[1;36mSee What's New on TWITTER\033[1;m", "=" * 20)
print("=" * 67)

# Authenticate against Twitter
auth = tweepy.OAuthHandler("your_consumer_key", "your_consumer_key_secret")
auth.set_access_token("your_access_token", "your_access_token_secret")

api = tweepy.API(auth)

# Read 20 most recent tweets from your timeline.
public_tweets = api.home_timeline()

for tweet in public_tweets:
    twitterData = "\033[1;36m> \033[1;m" + tweet.user.name + "| " + tweet.text
    print(twitterData)

print("=" * 67)
print("=" * 67)

# Send tweet
yourTweet = input("\033[1;32mWhat's Happening:\033[1;m ")
print("=" * 67)
api.update_status(yourTweet + " #twitterbot" + (emojize(":rocket:")))
print("Posted!! ", (emojize(":thumbs_up:")))


