#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from plugins.plugin import Plugin
from components.constants import *


class Haar(Plugin):
  
    def __init__(self):
        self.depth = 1
        self.color = "#ffff00000000"
        self.comment = self.getHelp()
        pass
        
    def set_properties(self, data):
        #Escrever o XML
        self.depth = data["0"]
        self.color = data["1"]
        self.comment = data["2"]
        print "Este é o haar" + str(data)

    def get_properties(self):
        #Ler do XML
        return {"0": {"name":"Depth",
                            "type": HARPIA_INT,
                            "lower":0,
                            "step" :1,
                            "upper":10,
                            "value":self.depth},
                "1": {"name":"Back Ground",
                            "type": HARPIA_COLOR,
                            "value":self.color
                            },
                "2": {"name":"Comment",
                            "type": HARPIA_COMMENT,
                            "height":150,
                            "width":500,
                            "value":self.comment}
                }

    def getHelp(self):
        return "Operacão de filtragem que implementa o algoritmo Canny para detecção de contornos e bordas.\nPropriedades\nLimiar 1 e Limiar 2: os dois valores de limiar são utilizados em conjunto. O menor valor é utilizado para a realizar a conexão de cantos e bordas. O maior valor é utilizado para encontrar segmentos iniciais das bordas mais significativas."

        
