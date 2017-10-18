# -*- coding: utf-8 -*-
'''
Created on 22 de mai de 2017

@author: ik
'''
#    Modelo do objeto retornado pelo send_msg enviado pela classe sa_api
#    Aqui é colocado já no construtor o respectivo campo do json analisado pelu buffer recebido
#    Foi colocado também um print object para facilitar a visualização

class sentimentModel():
    def __init__(self, confidence, irony, agreement, score_tag, subjectivity):
        self.__confidence = confidence
        self.__irony = irony
        self.__agreement = agreement
        self.__score_tag = score_tag
        self.__subj = subjectivity
        
    def print_object(self):
        print('CONFIDENCE:%s\nIRONY:%s\nAGREEMENT:%s\nSCORE_TAG:%s\nSUBJECTIVITY:%s'
            %(self.__confidence, 
            self.__irony,
            self.__agreement,
            self.__score_tag,
            self.__subj))