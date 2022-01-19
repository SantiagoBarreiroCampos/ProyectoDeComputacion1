# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:57 2022

@author: Yago
"""
import os
from CreadorDF import CreadorDF

creador = CreadorDF()

paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio", os.getcwd() + "\\Unlabeled"]

tablaTrain, palabras = creador.creadorDFTrain(paths[0], paths[1])
tablaTest = creador.creadorDFTest(paths[2])
print(tablaTrain)
print(tablaTest)


def EntrenarSVM():
    return 0
