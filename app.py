from argparse import Action
from ast import Global
from cgitb import enable, text
from collections import defaultdict
from ctypes import sizeof
from ctypes.wintypes import SIZE
from email.policy import default
from faulthandler import disable
from msilib import Table
import os
import string
from this import d
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from turtle import left, width
from unittest import TestCase
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sympy import C
from CreadorDF import CreadorDF
from TEST import TEST
from TRAIN import *
from joblib import dump, load
import pickle
from os import remove





def abrir_dir():
    

    directorio=filedialog.askdirectory(title="selecciona directorio")

  


    return directorio

def abrirarchivo(x,Rutanoticiasclasificar,framedelatabla):

    global tabladenoticias
    global dfTest
    global nombresnoticias
    global noticiasmostrar


    directorio=filedialog.askopenfile(title="selecciona el modelo")
  
    x.delete(0,"end")
    x.insert(0,directorio.name)
    x.textvariable=directorio.name
    
    #usar modelo
    
    x=open(directorio.name,"rb")
    
    loaded_model = pickle.load(x)

    dirarchivolistaplabras=directorio.name
    dirarchivolistaplabras =dirarchivolistaplabras.replace(".joblib", ".txt")




    dfTest=ejecutarTest(Rutanoticiasclasificar, loaded_model,dirarchivolistaplabras)




    tabladenoticias=ttk.Treeview(framedelatabla,columns = ('#1','#2','#3'),show='headings',selectmode ='browse')

    scroll=Scrollbar(framedelatabla,command=tabladenoticias.yview)
    scroll.pack(side="right", fill="y")
    
    tabladenoticias.configure(yscrollcommand = scroll.set)
    tabladenoticias.heading("#1",text="Noticia")
    tabladenoticias.heading("#2",text="Categoria")
    tabladenoticias.heading("#3",text="Ver")

    
    nombresnoticias=[]
    noticiasmostrar=[]
    
    
    files = os.listdir(Rutanoticiasclasificar)
    arrayNoticias = []
    
    for file in files:
        file_path = os.path.join(Rutanoticiasclasificar, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding="ISO 8859-1") as f:
                
                fileread = f.read()
                noticiasmostrar.append(fileread)
                
                nombresnoticias.append(file)
    
                
    
    i=0
    #
    for nombre in nombresnoticias:

        tabladenoticias.insert(parent='',index='end',iid=i,values=(nombresnoticias[i],dfTest["CATEGORIA"][i],"ver"))
        i=i+1


    tabladenoticias.pack(fill="x")




    return x


  

def mostrarnoticia():



    noticia=Toplevel()
    noticia.title("APP CLASIFICADORA")

    noticia.geometry('740x500')
    noticia.resizable(1,1)


    return 0
def carpeta(x):

    dir=abrir_dir()
    x.delete(0,"end")
    x.insert(0,dir)
    x.textvariable=dir

    global listanoticias
    listanoticias=dir


    
    return x,dir

def carpetaTEST(x):

    dir=abrir_dir()
    x.delete(0,"end")
    x.insert(0,dir)
    x.textvariable=dir

    global listanoticiasunlabeled
    listanoticiasunlabeled=dir


    
    return x,dir

def activarbtn(Bseleccionarmodeloclasificador):

    Bseleccionarmodeloclasificador['state'] = tk.NORMAL

    return 1


def prop(n):
    return 360.0 * n / 100

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
    
    n=float(preci)

    canvas1 =tk.Canvas(matrizdisper, width = 50, height = 50)
    canvas1.pack()
    blue=prop(n)
    red=prop(100-n)
    canvas1.create_arc((2,2,48,48), fill="#0000ff", outline="#0000ff", start=prop(0), extent = blue)
    canvas1.create_arc((2,2,48,48), fill="#ff0000", outline="#ff0000", start=blue, extent = red)
    canvas1.place(relx=0.9,rely=0.5,anchor=CENTER)

    return 0

def ejecutarTest(pathUnlabeled, clfloaded,dirarchivolistaplabras):


    algoritmo=TEST()
    
    #listapalabras

    with open(dirarchivolistaplabras) as f:
        text = f.read()
        listapalabras = text.split("\n")
    



    dfTest=algoritmo.Test(pathUnlabeled, clfloaded,listapalabras)




    return dfTest

def guardar(x):



    directorio = filedialog.asksaveasfilename(defaultextension=".joblib",title="Save",filetypes=(("pickel clf", "*.joblib"),("all files", "*.*")))
                    

    x.delete(0,"end")
    x.insert(0,directorio)
    x.textvariable=directorio
    
    print(directorio)
    pickle.dump(clf, open(directorio, 'wb')) 

    archivolistaplabras=directorio

    archivolistaplabras = archivolistaplabras.replace(".joblib", ".txt")

    print(archivolistaplabras)

    if (os.path.isfile(archivolistaplabras)):
        remove(archivolistaplabras)
    
    file = open(archivolistaplabras, "w")
    for word in listapalabra:
        file.write(word+"\n")


    
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
RutanoticiasUnlabel=os.getcwd()+"\\Unlabeled"

#seleccionar elementos entrenamiento

LnoticiasOdioEntreno=Label(p1,text='Noticias Odio:')
LnoticiasOdioEntreno.place(relx=0.1,rely=0.1 , anchor=CENTER)

LnoticiasNoOdioEntreno=Label(p1,text='Noticias No Odio:')
LnoticiasNoOdioEntreno.place(relx=0.1,rely=0.2 , anchor=CENTER)

RutanoticiasOdiolabel = StringVar()
LnoticiasOdioEntrenoruta=Entry(p1,text='Ruta',width = 60, textvariable=RutanoticiasOdiolabel)
LnoticiasOdioEntrenoruta.place(height=19,relx=0.5,rely=0.1,anchor=CENTER)


BnoticiasOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasOdioEntrenoruta))
BnoticiasOdioEntrenoruta.place(relx=0.9,rely=0.1,anchor=CENTER)


RutanoticiasNOOdiolabel = StringVar()
LnoticiasNoOdioEntrenoboton=Entry(p1,text='Ruta',width = 60, textvariable=RutanoticiasNOOdiolabel)
LnoticiasNoOdioEntrenoboton.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

BnoticiasNoOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:carpeta(LnoticiasNoOdioEntrenoboton))
BnoticiasNoOdioEntrenoruta.place(relx=0.9,rely=0.2,anchor=CENTER)


#barra algoritmos
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



ejecutartrain=Button(p1,text="Ejecutar",command=lambda:ejecutar(variablealgoritmo.get(),RutanoticiasOdiolabel.get(),RutanoticiasNOOdiolabel.get(),informacionalgoritmo,matrizdisper))
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




RutaModeloclf = StringVar()
Lclasificador=Entry(p2,text='ruta',width = 60, textvariable=RutaModeloclf)
Lclasificador.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

tablita=Frame(p2,bg="white")
tablita.place(height=250,width=450,relx=0.35,rely=0.6,anchor=CENTER)

Bseleccionarmodeloclasificador=Button(p2,text="Modelo",command=lambda:abrirarchivo(Lclasificador,Rutanoticiasclasificar.get(),tablita),state=tk.DISABLED)
Bseleccionarmodeloclasificador.place(relx=0.9,rely=0.2,anchor=CENTER)








#agregamos pestañas


nb.add(p1,text='entrenamiento')
nb.add(p2,text='clasificacion')



root.mainloop()

#fin interfaz


