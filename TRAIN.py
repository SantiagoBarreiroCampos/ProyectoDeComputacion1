# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:57 2022

@author: Yago
"""
import os
from CreadorDF import CreadorDF








def dataFrameEntrenamiento(pathOdio, pathNoOdio):
    creador = CreadorDF()
    tablaTrain, palabras = creador.creadorDFTrain(pathOdio, pathNoOdio)
    return tablaTrain, palabras

def EntrenarSVM():
    return 0


paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio", os.getcwd() + "\\Unlabeled"]
dfEntrenamiento, listapalabras = dataFrameEntrenamiento(paths[0], paths[1])

print(dfEntrenamiento)