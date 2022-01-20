from argparse import Action
from ast import Global
from cgitb import enable, text
from ctypes import sizeof
from ctypes.wintypes import SIZE
from faulthandler import disable
import os
from this import d
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from turtle import left
import numpy as np
import pandas as pd
from pyrsistent import b
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

from sympy import C
from CreadorDF import CreadorDF
from TRAIN import *
from joblib import dump, load
import pickle






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




def ejecutar(x,rutaOdio,rutaNoOdio,informacionalgoritmo,matrizdisper):

    LNejemplaresOdio=Label(informacionalgoritmo,text=len([name for name in os.listdir(rutaOdio)]),font=('Arial',7)).place(relx=0.6,rely=0.2,anchor=W)
    LNejemplaresNoOdio=Label(informacionalgoritmo,text=len([name for name in os.listdir(rutaNoOdio)]),font=('Arial',7)).place(relx=0.6,rely=0.4,anchor=W)
    LNtotal=Label(informacionalgoritmo,text=(len([name for name in os.listdir(rutaOdio)])+len([name for name in os.listdir(rutaNoOdio)])),font=('Arial',7)).place(relx=0.6,rely=0.6,anchor=W)
    Lalgoritmo=Label(informacionalgoritmo,text=x,font=('Arial',7)).place(relx=0.6,rely=0.8,anchor=W)


    



    global clf
    global matrizdis
    global preci
    global listapalabra



    algoritmo=TRAIN()
    print(x)

    clf,matrizdis,preci,listapalabra=algoritmo.Train(rutaOdio,rutaNoOdio,x)

    
    a=str(matrizdis[0][0])
    b=str(matrizdis[0][1])
    c=str(matrizdis[1][0])
    d=str(matrizdis[1][1])
    
    
    imprimirM="Verdaderos Positivos:"+a+"  Falsos Positivos:"+b+"\n"+"Falsos Negativos:"+c+"  Verdaderos Negativos:"+d
    LMatriz=Label(matrizdisper,text=imprimirM,font=('Arial',10)).place(relx=0.5,rely=0.5,anchor=CENTER)
    
   
   


    return 0



def guardar(x):



    directorio = filedialog.asksaveasfilename(defaultextension=".joblib",title="Save",filetypes=(("pickel clf", "*.joblib"),("all files", "*.*")))
                    

    x.delete(0,"end")
    x.insert(0,directorio)
    x.textvariable=directorio
    
    
    dump(clf, directorio) 
    


    
    return x,directorio




root = Tk()

#interfaz 
root.title("APP CLASIFICADORA")

root.geometry('740x500')
root.resizable(0,0)

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
LnoticiasOdioEntrenoruta=Entry(p1,text='Ruta',width = 60, textvariable=RutanoticiasOdiolabel)
LnoticiasOdioEntrenoruta.place(height=19,relx=0.5,rely=0.1,anchor=CENTER)


BnoticiasOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasOdioEntrenoruta,RutanoticiasOdio))
BnoticiasOdioEntrenoruta.place(relx=0.9,rely=0.1,anchor=CENTER)


RutanoticiasNOOdiolabel = StringVar()
LnoticiasNoOdioEntrenoboton=Entry(p1,text='Ruta',width = 60, textvariable=RutanoticiasNOOdiolabel)
LnoticiasNoOdioEntrenoboton.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

BnoticiasNoOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasNoOdioEntrenoboton,RutanoticiasNOOdio))
BnoticiasNoOdioEntrenoruta.place(relx=0.9,rely=0.2,anchor=CENTER)

OptionList = [
"Decision Tree",
"SVM",
"Naive Bayes",

] 





variablealgoritmo = tk.StringVar(p1)
variablealgoritmo.set(OptionList[0])



opt = tk.OptionMenu(p1, variablealgoritmo, *OptionList)
opt.config(width=40)
opt.place(relx=0.3,rely=0.3,anchor=CENTER)













#recuadro con la info

informacionalgoritmo=Frame(p1)
informacionalgoritmo.config(width=300,height=130,background="white",relief=tk.FLAT,bd=20,highlightthickness=4) 
informacionalgoritmo.place(relx=0.3,rely=0.5,anchor=CENTER)

Lvistaprevia=Label(informacionalgoritmo,text="VISTA PREVIA:",font=('Arial',9)).place(relx=0.1,rely=0,anchor=CENTER)
Lvistaprevia1=Label(informacionalgoritmo,text="Ejemplares odio:",font=('Arial',7)).place(relx=0.1,rely=0.2,anchor=W)
Lvistaprevia2=Label(informacionalgoritmo,text="Ejemplares No odio:",font=('Arial',7)).place(relx=0.1,rely=0.4,anchor=W)
Lvistaprevia3=Label(informacionalgoritmo,text="Total:",font=('Arial',7)).place(relx=0.1,rely=0.6,anchor=W)
Lvistaprevia4=Label(informacionalgoritmo,text="Algoritmo seleccionado:",font=('Arial',7)).place(relx=0.1,rely=0.8,anchor=W)

#fin recuadro
#recuadro 2

matrizdisper=Frame(p1)
matrizdisper.config(width=600,height=90,background="white",relief=tk.FLAT,bd=20,highlightthickness=4) 
matrizdisper.place(relx=0.1,rely=0.7)

LResultado=Label(matrizdisper,text="Resultados:",font=('Arial',12)).place(relx=0.1,rely=0,anchor=CENTER)


#fin recuadro 2



ejecutartrain=Button(p1,text="Ejecutar",command=lambda:ejecutar(variablealgoritmo.get(),RutanoticiasOdio,RutanoticiasNOOdio,informacionalgoritmo,matrizdisper))
ejecutartrain.place(relx=0.9,rely=0.4,anchor=CENTER)

#guardar

Lguardar=Label(p1,text="Guardar Modelo:").place(relx=0.1,rely=0.9)



Rdirguardar = StringVar()
Lguardardir=Entry(p1,text='Ruta',width = 60, textvariable=Rdirguardar)
Lguardardir.place(height=19,relx=0.5,rely=0.925,anchor=CENTER)

BGuardarmodelo=Button(p1,text="Guardar",command=lambda:guardar(Lguardardir))
BGuardarmodelo.place(relx=0.9,rely=0.925,anchor=CENTER)


#fin guardar





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


