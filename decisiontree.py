from argparse import Action
from cgitb import enable, text
from faulthandler import disable
import os
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from turtle import left
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import requests
import os
from io import open
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics  import f1_score,accuracy_score
from CreadorDF import CreadorDF

class decisiontree:

    def decisiontree(pathOdio,pathNoOdio):


        creador = CreadorDF()
        dfTotal=creador.creadorDFTrain(pathOdio, pathNoOdio)




        iris = load_iris()
        X, y = iris.data, iris.target
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(dfTotal["data"],dfTotal["Odio"])

        pred = clf.predict(dfTotal["data"])
        print(pred.tolist())


        print(f1_score(dfTotal["Odio"],pred,average='micro'))


        return 0


































