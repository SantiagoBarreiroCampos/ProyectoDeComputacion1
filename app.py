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
from CreadorDF import CreadorDF
from decisiontree import decisiontree






def abrir_dir():


    directorio=filedialog.askdirectory(title="selecciona directorio")
    if directorio!="":
        os.chdir(directorio)
  

    return os.getcwd()

def abrirarchivo(x):


    directorio=filedialog.askopenfile(title="selecciona el modelo")
  
    x.delete(0,"end")
    x.insert(0,directorio)
    x.textvariable=directorio

    #ejecutar

    return x

def carpeta(x):

    dir=abrir_dir()
    x.delete(0,"end")
    x.insert(0,dir)
    x.textvariable=dir

  
    return x

def activarbtn(Bseleccionarmodeloclasificador):

    Bseleccionarmodeloclasificador['state'] = tk.NORMAL

    return 1




def ejecutar(x,rutaOdio,rutaNoOdio):

    if x=="Decision Tree":
        y=decisiontree(rutaOdio,rutaNoOdio)
    elif x=="supportvectormachinegenmodel":
        y=supportvectormachinegenmodel(rutaOdio,rutaNoOdio)
    elif x=="NaiveBayesgenmodel":
        y=NaiveBayesgenmodel(rutaOdio,rutaNoOdio)

    return 0






root = Tk()

#interfaz 
root.title("APP CLASIFICADORA")

root.geometry('740x400')
root.resizable(0,0)

nb=ttk.Notebook(root)
nb.pack(fill='both',expand=YES)


p1=ttk.Frame(nb)
p2=ttk.Frame(nb)



#elementos entrenamiento

LnoticiasOdioEntreno=Label(p1,text='Noticias Odio:')
LnoticiasOdioEntreno.place(relx=0.1,rely=0.1 , anchor=CENTER)

LnoticiasNoOdioEntreno=Label(p1,text='Noticias No Odio:')
LnoticiasNoOdioEntreno.place(relx=0.1,rely=0.2 , anchor=CENTER)

RutanoticiasOdio = StringVar()
LnoticiasOdioEntrenoruta=Entry(p1,text='ruta',width = 60, textvariable=RutanoticiasOdio )
LnoticiasOdioEntrenoruta.place(height=19,relx=0.5,rely=0.1,anchor=CENTER)


BnoticiasOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasOdioEntrenoruta))
BnoticiasOdioEntrenoruta.place(relx=0.9,rely=0.1,anchor=CENTER)


RutanoticiasNOOdio = StringVar()
LnoticiasNoOdioEntrenoboton=Entry(p1,text='ruta',width = 60, textvariable=RutanoticiasNOOdio)
LnoticiasNoOdioEntrenoboton.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

BnoticiasNoOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasNoOdioEntrenoboton))
BnoticiasNoOdioEntrenoruta.place(relx=0.9,rely=0.2,anchor=CENTER)

OptionList = [
"generalizedlinearmodelgenmodel",
"supportvectormachinegenmodel",
"NaiveBayesgenmodel",

] 

variable = tk.StringVar(root)
variable.set(OptionList[0])

opt = tk.OptionMenu(root, variable, *OptionList)
opt.config(width=40)
opt.place(relx=0.3,rely=0.4,anchor=CENTER)


#elementos clasificacion


Lnoticiasparaclasificar=Label(p2,text='Noticias para clasificar:')
Lnoticiasparaclasificar.place(relx=0.1,rely=0.1 , anchor=CENTER)


LModeloclasificador=Label(p2,text='Modelo clasificador:')
LModeloclasificador.place(relx=0.1,rely=0.2 , anchor=CENTER)

Rutanoticiasclasificar = StringVar()
Lnoticiasparaclasificarruta=Entry(p2,text='ruta',width = 60, textvariable=Rutanoticiasclasificar )
Lnoticiasparaclasificarruta.place(height=19,relx=0.5,rely=0.1,anchor=CENTER)

Bseleccionarnoticiasrutasparaclasificar=Button(p2,text="Abrir",command=lambda:[carpeta(Lnoticiasparaclasificarruta),activarbtn(Bseleccionarmodeloclasificador)])
Bseleccionarnoticiasrutasparaclasificar.place(relx=0.9,rely=0.1,anchor=CENTER)




Rutaclasificador = StringVar()
Lclasificador=Entry(p2,text='ruta',width = 60, textvariable=Rutaclasificador)
Lclasificador.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

Bseleccionarmodeloclasificador=Button(p2,text="Abrir",command=lambda:abrirarchivo(Lclasificador),state=tk.DISABLED)
Bseleccionarmodeloclasificador.place(relx=0.9,rely=0.2,anchor=CENTER)




#agregamos pestañas


nb.add(p1,text='entrenamiento')
nb.add(p2,text='clasificacion')



root.mainloop()

#fin interfaz


