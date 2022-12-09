#!/usr/bin/env python
# encoding: utf-8
import json

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [tweet.lang for tweet in alltweets]

	lang_code = ""
	#print(json.dumps(alltweets[0], indent=4, sort_keys=True, default=str))
	j = json.dumps(outtweets, indent=4, sort_keys=True, default=str, separators=(',', ': '))
	for tweet in outtweets:
		if tweet != None:
			lang_code += tweet
		else:
			lang_code += "<NULL>"
	print(lang_code)
	pass

import datetime

def default(o):
	if isinstance(o, (datetime.date, datetime.datetime)):
		return o.isoformat()

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("1231507051321")
