
# Developed by Henrique Lobato
# ikk.lobs@gmail.com

'''
Created on 22 de mai de 2017

@author: ik
'''

from tweepy import Stream
from tweepy import OAuthHandler

from sa_api import sentimentAnalysis
from sentiment_model import sentimentModel
from tweet_model import tweetModel
from twitter_api import twitterApi as twt_api_class

CKEY = 'your CSKEY'
CSECRET = 'your CSECRET'
ATOKEN = 'you ATOKEN'
ASECRET = 'your ASECRET'
TEXT = 'listening worldwide for this string or word when running...'

if __name__ == "__main__":
    
    auth = OAuthHandler(CKEY, CSECRET)
    auth.set_access_token(ATOKEN, ASECRET)
    twitterStream = Stream(auth, twt_api_class(), timeout=60)
    try:
        twitterStream.filter(track=[TEXT])
    except Exception as e:
        print(format(e))
        print(type(e))
    
    print('')
