# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:57 2022

@author: Yago
"""
import os
from TRAIN import TRAIN

entrenamiento = TRAIN()

paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio"]
algoritmo = "Naive Bayes"

clf, matriz, precision, palabras = entrenamiento.Train(paths[0], paths[1], algoritmo)
#tabla, palabras = creador.creadorDF(paths[0], paths[1])

print("\n----------DEVUELTO----------\n")
print(matriz)
print(precision)
#print(palabras)
