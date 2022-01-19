from argparse import Action
from cgitb import enable, text
from ctypes import sizeof
from ctypes.wintypes import SIZE
from faulthandler import disable
import os
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import font
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
from TRAIN import *







def abrir_dir():


    directorio=filedialog.askdirectory(title="selecciona directorio")
    if directorio!="":
        os.chdir(directorio)
  

    return directorio

def abrirarchivo(x):


    directorio=filedialog.askopenfile(title="selecciona el modelo")
  
    x.delete(0,"end")
    x.insert(0,directorio)
    x.textvariable=directorio

    #ejecutar

    return x

def carpeta(x,dir):

    dir=abrir_dir()
    x.delete(0,"end")
    x.insert(0,dir)
    x.textvariable=dir

    
    return x,dir

def activarbtn(Bseleccionarmodeloclasificador):

    Bseleccionarmodeloclasificador['state'] = tk.NORMAL

    return 1




def ejecutar(x,rutaOdio,rutaNoOdio):

    algoritmo=TRAIN()


    clf,matrizdis,preci,listapalabra=algoritmo.Train(rutaOdio,rutaNoOdio,x)




    return clf,matrizdis,preci,listapalabra






root = Tk()

#interfaz 
root.title("APP CLASIFICADORA")

root.geometry('740x500')
root.resizable(1,1)

nb=ttk.Notebook(root)
nb.pack(fill='both',expand=YES)


p1=ttk.Frame(nb)
p2=ttk.Frame(nb)

RutanoticiasOdio=os.getcwd()+"\\Odio"
RutanoticiasNOOdio=os.getcwd()+"\\NoOdio"

#elementos entrenamiento

LnoticiasOdioEntreno=Label(p1,text='Noticias Odio:')
LnoticiasOdioEntreno.place(relx=0.1,rely=0.1 , anchor=CENTER)

LnoticiasNoOdioEntreno=Label(p1,text='Noticias No Odio:')
LnoticiasNoOdioEntreno.place(relx=0.1,rely=0.2 , anchor=CENTER)

RutanoticiasOdiolabel = StringVar()
LnoticiasOdioEntrenoruta=Entry(p1,text='ruta',width = 60, textvariable=RutanoticiasOdiolabel )
LnoticiasOdioEntrenoruta.place(height=19,relx=0.5,rely=0.1,anchor=CENTER)


BnoticiasOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasOdioEntrenoruta,RutanoticiasOdio))
BnoticiasOdioEntrenoruta.place(relx=0.9,rely=0.1,anchor=CENTER)


RutanoticiasNOOdiolabel = StringVar()
LnoticiasNoOdioEntrenoboton=Entry(p1,text='ruta',width = 60, textvariable=RutanoticiasNOOdiolabel)
LnoticiasNoOdioEntrenoboton.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

BnoticiasNoOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasNoOdioEntrenoboton,RutanoticiasNOOdio))
BnoticiasNoOdioEntrenoruta.place(relx=0.9,rely=0.2,anchor=CENTER)

OptionList = [
"Decision Tree",
"SVM",
"Naive Bayes",

] 

variable = tk.StringVar(root)
variable.set(OptionList[0])

opt = tk.OptionMenu(p1, variable, *OptionList)
opt.config(width=40)
opt.place(relx=0.3,rely=0.3,anchor=CENTER)


ejecutartrain=Button(p1,text="Ejecutar",command=lambda:ejecutar(variable,RutanoticiasOdio,RutanoticiasNOOdio))
ejecutartrain.place(relx=0.9,rely=0.4,anchor=CENTER)




#recuadro con la info
informacionalgoritmo=Frame(p1)
informacionalgoritmo.config(width=300,height=130,background="white",relief=tk.FLAT,bd=20,highlightthickness=4) 
informacionalgoritmo.place(relx=0.3,rely=0.5,anchor=CENTER)

Lvistaprevia=Label(informacionalgoritmo,text="VISTA PREVIA:",font=('Arial',9)).place(relx=0.1,rely=0,anchor=CENTER)
Lvistaprevia1=Label(informacionalgoritmo,text="Ejemplares odio:",font=('Arial',7)).place(relx=0.1,rely=0.2,anchor=W)
Lvistaprevia2=Label(informacionalgoritmo,text="Ejemplares No odio:",font=('Arial',7)).place(relx=0.1,rely=0.4,anchor=W)
Lvistaprevia3=Label(informacionalgoritmo,text="Total:",font=('Arial',7)).place(relx=0.1,rely=0.6,anchor=W)
Lvistaprevia4=Label(informacionalgoritmo,text="Algoritmo seleccionado:",font=('Arial',7)).place(relx=0.1,rely=0.8,anchor=W)

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


