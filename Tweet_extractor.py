# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 22:35:43 2017

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 12:05:14 2017

@author: asus
"""

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '345897530-7MndmcGDFgyE0m4dZWW0XbhtRv8oeUBlbUvoBVFm'
ACCESS_SECRET = 'FDWwMg0zdWqnG1hbcxUM18gmPGj3DeMZZQYHOXhDWRHtS'
CONSUMER_KEY = 'w2DwAT2cisfGVhDFMv5fHjwXA'
CONSUMER_SECRET = '7VzsDseQ9VrIHTpvvTSIaetdHtuX6p2Fh62dBeNE4KL0vckKqb'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10000000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
