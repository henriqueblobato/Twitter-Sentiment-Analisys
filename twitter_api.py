# -*- coding: utf-8 -*-
'''
Created on 22 de mai de 2017

@author: ik
'''
import json
import traceback
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.error import TweepError
from tweet_model import tweetModel

#    Classe que faz o recebimento em streaming dos tweets sob uma determinada palavra ou frase
#    Após criar a autenticação OAuth (usando ckey e csecret) é utilizado esse objeto para
#        fazer a autenticação do token (atoken e asecret)
#    Depois é criado um objeto stream passando o parâmetro de autenticação e a classe que
#        possui o método on_data(), que funcionará como callback
#    A ativação do streaming acontece no .filter(track=['lista de palavras chave'])
#    O tratamento do buffer recebido em json acontece dentro do on_data

CKEY = 'YOUR CKEY'
CSECRET = 'YOUR CSECRET'
ATOKEN = 'YOUR ATOKEN'
ASECRET = 'YOUR ASECRET'

STREAM_TIMEOUT = 60

class twitterApi(StreamListener):
    
    def __init__(self):
        self.__auth = (OAuthHandler(CKEY, CSECRET))
        (self.__auth).set_access_token(ATOKEN, ASECRET)
        try:
            self.__stream = Stream(self.__auth, self, timeout=STREAM_TIMEOUT)
        except Exception as e:
            print(format(e))
        
    def get_stream(self):
        return self.__stream
    
    def on_data(self, data):
        if 'created_at' in data:
            try:
                #print(json.loads(data))
                obj = self.mount_tweet_model(json.loads(data))
                obj.print_final_object()
                #obj.print_in_file()
            except Exception as e:
                traceback.print_exc()
                print(format(e))
                print(type(e))
        else:
            print('Keep alive')
     
    def print_result(self, data):
        print('TEXT:%s\nUSER NAME:%s\nUSER FOLLOWERS:%s\nUSER LOCATION:%s\nLANGUAGE:%s\nRETWEETED:%s\nGEO:%s\n'
                    %(data['text'], 
                      data['user']['screen_name'],
                      data['user']['followers_count'],
                      data['user']['time_zone'],
                      data['lang'],
                      data['retweeted'],
                      data['geo']))
        
    def mount_tweet_model(self, data):
        return tweetModel(data['text'],
                               data['user']['screen_name'],
                               data['user']['followers_count'],
                               data['user']['time_zone'],
                               data['lang'],
                               data['retweeted'],
                               data['geo']) 


#if __name__ == "__main__":
#    text = 'temer'
#    
#    auth = OAuthHandler(CKEY, CSECRET)
#    auth.set_access_token(ATOKEN, ASECRET)
#   twitterStream = Stream(auth, twitterApi(), timeout=60)
#    try:
#        twitterStream.filter(track=[text])
#    except Exception as e:
#        print(format(e))
#        print(type(e))
