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



root = Tk()


def generateDF(path):
    
    df = pd.DataFrame({"name": [], "path": [], "content":[]})
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        

        
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding="ISO 8859-1") as f:
                
                spiltfile=f.read();
                splitedcontent = spiltfile.split("#####")#0=link 1=autor 2=fecha 3=titulo 4=content
                #juntar title y content           #####
                content=splitedcontent[3]+" "+splitedcontent[4]+" "+splitedcontent[5]
                
                
                df = df.append({"name": file, "path": file_path,"content":content }, ignore_index=True)
        elif os.path.isdir(file_path):
            df = df.append(generateDF(file_path))
            

            
            
 
    
    
    return df

def tokenize(x):
    return RegexpTokenizer(r'\w+').tokenize(x.lower())

def removeStopwords(x):
    z=["prueba"]
    with open("listaParadaEsp.txt") as f:
        text = f.read()
        prohibitedWords = text.split("\n")
        
        y=[word for word in x if not word in prohibitedWords]
        
        for word in y:
            word = re.sub("(\d+)","",word)
            z = np.append(z, word)
                
        return z

def stemming(x):
    
    stemmer = SnowballStemmer(language="spanish")
    
    return ' '.join([stemmer.stem(word)for word in x])





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

def generalizedlinearmodelgenmodel(rutaOdio,rutaNoOdio):

    dfOdio=generateDF(rutaOdio)
    dfNoOdio=generateDF(rutaNoOdio)

    x=dfOdio['content'].map(tokenize)
    x=x.map(removeStopwords)
    x=x.map(stemming)
    vectorizerx = TfidfVectorizer()
    X = vectorizerx.fit_transform(x)
    nombresx = vectorizerx.get_feature_names()
    arrayx = X.toarray()


    y=dfNoOdio['content'].map(tokenize)
    y=y.map(removeStopwords)
    y=y.map(stemming)
    vectorizery = TfidfVectorizer()
    Y = vectorizery.fit_transform(y)
    nombresy = vectorizery.get_feature_names()
    arrayy = Y.toarray()







    tablaNoOdio = pd.DataFrame(data = arrayy,columns=nombresy)
    tablaOdio = pd.DataFrame(data = arrayx,columns=nombresx)



    clf = linear_model.LinearRegression().fit(tablaNoOdio,tablaOdio)
  


    return 0

def supportvectormachinegenmodel(rutaA,rutaB):



    return 0

def NaiveBayesgenmodel(rutaA,rutaB):



    return 0











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


