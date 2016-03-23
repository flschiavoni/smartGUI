#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from plugins.plugin import Plugin
from components.constants import *


class Dilatacao(Plugin):
  
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        pass
        
    def set_properties(self, data):
        #Escrever o XML
        self.x = data["0"]
        self.y = data["1"]
        self.w = data["2"]
        self.h = data["3"]

        print "Este é o dilatação" + str(data)

    def get_properties(self):
        #Ler do XML
        return {"0":{"name": "X",
                            "type": HARPIA_INT,
                            "lower":0,
                            "upper":10,
                            "step" :1,
                            "value":self.x},
                "1":{"name": "Y",
                            "type": HARPIA_INT,
                            "lower":0,
                            "upper":10,
                            "step" :1,
                            "value":self.y},
                "2":{"name":"Width",
                            "type": HARPIA_INT,
                            "lower":0,
                            "upper":10,
                            "step" :1,
                            "value":self.w},
                "3": {"name":"Height",
                            "type": HARPIA_INT,
                            "lower":0,
                            "upper":10,
                            "step" :1,
                            "value":self.h}
                }

    def getHelp(self):
        return "Operação dilatenta profunda cartesiana e poliritmica.\n Rulez the world!"

        
