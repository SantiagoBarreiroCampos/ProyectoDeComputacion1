# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:11:12 2022

@author: Yago
"""
from CreadorDF import CreadorDF

class TEST:
    
    def dataFrameTest(self, pathUnlabeled, listapalabras):
        creador = CreadorDF()
        tablaTest = creador.creadorDFTest(pathUnlabeled, listapalabras)
        return tablaTest
    
    def Test(self, pathUnlabeled, algoritmo, listapalabras):
        #crear df test
        dfTest = self.dataFrameTest(pathUnlabeled, listapalabras)
        
        categorias = []
        #algoritmo.predict =clf.predict
        for categoria in algoritmo.predict(dfTest):
            if categoria == 1:
                categorias.append("Odio")
            elif categoria == 0:
                categorias.append("NoOdio")
        

        #insertar en la columna 0
        dfTest.insert(0, "CATEGORIA", categorias, True)
        #print(dfTest)
        return dfTest