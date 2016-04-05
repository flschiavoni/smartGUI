#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from plugins.plugin import Plugin
from constants import *

class Erosao(Plugin):

    def __init__(self):
        self.titulo = "Meu Titulo"
        self.autor = ""
        self.editora = ""
        self.qtde_paginas = 0
        self.ano = 2016
        self.preco = 49.99
        pass

    def set_properties(self, data):
        #Escrever o XML
        self.titulo         = data["0-titulo"]
        self.autor          = data["1-autor"]
        self.editora        = data["2-editora"]
        self.qtde_paginas   = data["3-qtde"]
        self.ano            = data["4-ano"]
        self.preco          = data["5-preco"]
        print "Este é o erosão" + str(data)

    def get_properties(self):
        #Ler do XML
        return {"0-titulo":{"name": "Título",
                            "type": HARPIA_STRING,
                            "value": self.titulo},
                "1-autor":{"name": "Autor",
                            "type": HARPIA_STRING,
                            "value": self.autor},
                "2-editora":{"name":"Editora",
                            "type": HARPIA_STRING,
                            "value": self.editora},
                "3-qtde": {"name":"Qtde Páginas",
                            "type": HARPIA_INT,
                            "lower":0,
                            "step" :1,
                            "upper":10,
                            "value":self.qtde_paginas},
                "4-ano": {"name":"Ano",
                            "type": HARPIA_INT,
                            "lower":1900,
                            "upper":2010,
                            "step" :1,
                            "value":self.ano},
            	"5-preco": {"name":"Preço",
                            "type": HARPIA_FLOAT,
                            "lower":0.0,
                            "upper":100.0,
                            "step" :0.1,
                            "value":self.preco,
                            "digits":2}
                }

    def getHelp(self):
        return "Operacão de filtragem que implementa o algoritmo Canny para detecção de contornos e bordas.\nPropriedades\nLimiar 1 e Limiar 2: os dois valores de limiar são utilizados em conjunto. O menor valor é utilizado para a realizar a conexão de cantos e bordas. O maior valor é utilizado para encontrar segmentos iniciais das bordas mais significativas."

        
