# -*- coding: utf-8 -*-
'''
Created on 22 de mai de 2017

@author: ik
'''
import requests
import json
import threading
from sentiment_model import sentimentModel
from unicodedata import normalize

#    Classe criada para fazer a análise de sentimento de uma frase
#    Ao utilizar o método send_msg('bla') é retornado um objeto do tipo sentiment_model
#        que possui um método print_object

text = 'esta nada mais é do que uma mensagem teste gerada por um ser humano qualquer'
class sentimentAnalysis():
    def __init__(self):
        self.__url = 'http://api.meaningcloud.com/sentiment-2.1/'
        self.__key = 'your meaningcloud API key'
        self.__headers = {'content-type':'application/x-www-form-urlencoded'}
        self.__payload = ''
    
    def send_msg(self, msg):
        try:
            self.__payload = 'key=%s&lang=auto&txt=%s&model=general' %(self.__key, self.remover_acentos(msg)) 
            response = requests.request('POST', self.__url, data=self.__payload, headers=self.__headers)
            if response.status_code == 200:
                response = json.loads(response.text)
                #print(response)
                if response is not None:
                    return sentimentModel(response['confidence'],
                                            response['irony'],
                                            response['agreement'],
                                            response['score_tag'],
                                            response['subjectivity'])
            else:
                return
        except Exception as e:
            return
    
    def remover_acentos(self, txt, codif='utf-8'):
        return normalize('NFKD', txt).encode('ASCII','ignore')
        
    def get_words(self, msg):
        msg = msg.split(' ')
        for i in msg:
            if ' ' in i:
                msg.pop(i)
                
if __name__ == "__main__":
    sentiment_obj = sentimentAnalysis()
    sentiment_model_obj = sentiment_obj.send_msg('mensagem teste qualquer, irrelevante')
    
    sentiment_model_obj.print_object()
    
    print('')
