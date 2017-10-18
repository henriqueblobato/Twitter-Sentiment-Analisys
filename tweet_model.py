# -*- coding: utf-8 -*-
'''
Created on 22 de mai de 2017

@author: ik
'''
from sa_api import sentimentAnalysis

class tweetModel():
    def __init__(self, text, user, followers, time, lang, ret, geo):
        self.__text = text
        self.__user = user
        self.__followers = followers
        self.__time = time
        self.__langue = lang
        self.__retweet = ret
        self.__geo = geo
        self.__user_url = ''    # Para fazer: COLOCAR EM ['user']['url']
        s = sentimentAnalysis()
        self.__analysis = s.send_msg(text)
                
    def print_final_object(self):
        print('\n[TWEET]\nTEXT:%s\nUSER NAME:@%s\nUSER FOLLOWERS:%s\nLANGUAGE:%s\nRETWEETED:%s\nGEO:%s' %
                      (self.__text,
                      self.__user,
                      self.__followers,
                      self.__langue,
                      self.__retweet,
                      self.__geo))
        if self.__analysis is not None:
            self.__analysis.print_object()

    def print_in_file(self):
        with open('teste.txt', 'w') as arq:
            arq.write('\n[TWEET]\nTEXT:%s\nUSER NAME:@%s\nUSER FOLLOWERS:%s\nLANGUAGE:%s\nRETWEETED:%s\nGEO:%s' %
                      (self.__text, 
                      self.__user,
                      self.__followers,
                      self.__langue,
                      self.__retweet,
                      self.__geo))
