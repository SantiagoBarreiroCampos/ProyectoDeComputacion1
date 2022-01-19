# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:57 2022

@author: Yago
"""
import os
from TRAIN import TRAIN
from TEST import TEST

entrenamiento = TRAIN()

paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio"]
pathUnlabeled = os.getcwd() + "\\Unlabeled"
algoritmo = "SVM"

clf, matriz, precision, listapalabras = entrenamiento.Train(paths[0], paths[1], algoritmo)

test = TEST()


dfTest = test.Test(pathUnlabeled, clf, listapalabras)

print("\n\nResultados de la clasificacion con el algoritmo "+algoritmo+":\n")
print(dfTest.CATEGORIA)