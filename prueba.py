# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:57 2022

@author: Yago
"""
import os
from CreadorDF import CreadorDF

creador = CreadorDF()

paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio"]

tabla, palabras = creador.creadorDF(paths[0], paths[1])

print(tabla)
