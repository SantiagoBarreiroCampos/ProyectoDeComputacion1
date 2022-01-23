import os
import tkinter as tk 
from tkinter import ttk
from tkinter import Tk
from tkinter import Scrollbar
from tkinter import W
from tkinter import CENTER
from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import StringVar
from tkinter import YES
from tkinter import BOTH
from tkinter import Label
from tkinter import filedialog
from io import open
from TEST import TEST
from TRAIN import TRAIN
import pickle
from os import remove
import pandas as pd



def abrir_dir():
    directorio=filedialog.askdirectory(title="selecciona directorio")
    return directorio

def OptionMenu_SelectionEvent(event):
    global clasificadorGlobal
    clasificadorGlobal = variablealgoritmo.get()
    

def OnDoubleClick(event):
    item = tabladenoticias.selection()
    #print('item:', item)
    #print('event:', event)
    #item = tabladenoticias.selection()
    array = tabladenoticias.item(item,"values")
    #type(array)
    #print(array[0])
    #return array[0]
    abrirNoticia(array[0])
    
def abrirNoticia(nombreArchivo):
    #print(rutaUnlabel)
    os.startfile(rutaUnlabel+"/"+nombreArchivo)
    return 0

def abrirarchivo(x,Rutanoticiasclasificar,framedelatabla):

    
    #Lalgoritmo=Label(informacionalgoritmo,text=x,font=('Arial',7)).place(relx=0.6,rely=0.8,anchor=W)

    global tabladenoticias
    global dfTest
    global nombresnoticias
    global noticiasmostrar
    global rutaUnlabel

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


    
    global GuardCSV
    




    tabladenoticias=ttk.Treeview(framedelatabla,columns = ('#1','#2','#3'),show='headings',selectmode ='browse')
    tabladenoticias.pack(expand=YES, fill=BOTH)
    

    scroll=Scrollbar(framedelatabla,command=tabladenoticias.yview)
    scroll.pack(side="right", fill="y")
    
    tabladenoticias.configure(yscrollcommand = scroll.set)
    tabladenoticias.heading("#1",text="Noticia")
    tabladenoticias.column("#1", minwidth=0, width=200, stretch=tk.NO)
    tabladenoticias.heading("#2",text="Categoria")
    tabladenoticias.column("#2", minwidth=0, width=125, stretch=tk.NO, anchor=tk.CENTER)
    tabladenoticias.heading("#3",text="Ver")
    tabladenoticias.column("#3", minwidth=0, width=125, stretch=tk.NO, anchor=tk.CENTER)
    

    i=0
    for nombre in dfTest.index:

        tabladenoticias.insert(parent='',index='end',iid=i,values=(nombre,dfTest["CATEGORIA"][i],"Ver"))
        i=i+1
    tabladenoticias.pack(fill="x")
    rutaUnlabel = Rutanoticiasclasificar
    tabladenoticias.bind("<<TreeviewSelect>>", OnDoubleClick) # single click, without "index out of range" error

    nOdio = len([name for name in dfTest['CATEGORIA'] if name == 'Odio'])
    nNoOdio = len([name for name in dfTest['CATEGORIA'] if name == 'NoOdio'])
    nTotal = len([name for name in dfTest['CATEGORIA']])


    LNtotal=Label(informacionalgoritmo2,text=nTotal,font=('Arial',7)).place(relx=0.6,rely=0.2,anchor=W)
    LNejemplaresOdio=Label(informacionalgoritmo2,text=nOdio,font=('Arial',7)).place(relx=0.6,rely=0.35,anchor=W)
    LNejemplaresNoOdio=Label(informacionalgoritmo2,text=nNoOdio,font=('Arial',7)).place(relx=0.6,rely=0.50,anchor=W)
    
    n=float((nOdio/nTotal)*100)
           
    canvas1 =tk.Canvas(informacionalgoritmo2, width = 50, height = 50)
    canvas1.pack()
    blue=prop(n)
    red=prop(100-n)
    canvas1.create_arc((2,2,48,48), fill="#0000ff", outline="#0000ff", start=prop(0), extent = blue)
    canvas1.create_arc((2,2,48,48), fill="#ff0000", outline="#ff0000", start=blue, extent = red)
    canvas1.place(relx=0.5,rely=0.8,anchor=CENTER)



 
    GuardCSV=pd.DataFrame(list(zip(dfTest.index, dfTest["CATEGORIA"])),columns =['Name', 'Categoria'])

 
    


    return x


  




def carpeta(x):

    dir=abrir_dir()
    x.delete(0,"end")
    x.insert(0,dir)
    x.textvariable=dir

    global listanoticias
    listanoticias=dir


    
    return x,dir



def activarbtn(Bseleccionarmodeloclasificador):

    Bseleccionarmodeloclasificador['state'] = tk.NORMAL

    return 1


def prop(n):
    return 360.0 * n / 100

def vistaPrevia(rutaOdio,rutaNoOdio,informacionalgoritmoo):
    if(rutaOdio!=''):
        LNejemplaresOdio=Label(informacionalgoritmo,text=len([name for name in os.listdir(rutaOdio)]),font=('Arial',7)).place(relx=0.6,rely=0.2,anchor=W)
    if(rutaNoOdio!=''):
        LNejemplaresNoOdio=Label(informacionalgoritmo,text=len([name for name in os.listdir(rutaNoOdio)]),font=('Arial',7)).place(relx=0.6,rely=0.4,anchor=W)
    if(rutaOdio!='' and rutaNoOdio!=''):
        LNtotal=Label(informacionalgoritmo,text=(len([name for name in os.listdir(rutaOdio)])+len([name for name in os.listdir(rutaNoOdio)])),font=('Arial',7)).place(relx=0.6,rely=0.6,anchor=W)
    #print(clasificadorGlobal)
    Lalgoritmo=Label(informacionalgoritmo,text=clasificadorGlobal,font=('Arial',7)).place(relx=0.6,rely=0.8,anchor=W)


    
def ejecutar(x,rutaOdio,rutaNoOdio,informacionalgoritmo,matrizdisper):

    
    vistaPrevia(rutaOdio, rutaNoOdio, informacionalgoritmo)


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

def guardartest(x,GuardCSV):



    directorio = filedialog.asksaveasfilename(defaultextension=".joblib",title="Save",filetypes=(("csv", "*.csv"),("all files", "*.*")))
                    

    x.delete(0,"end")
    x.insert(0,directorio)
    x.textvariable=directorio
    

    Testcsv=GuardCSV.to_csv()

    file = open(directorio, "w")

    file.write(Testcsv)
    


    print(Testcsv)

   


    
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

global rutaOdioGlobal
global rutaNoOdioGlobal
global rutaUnlabelGlobal
global clasificadorGlobal
#RutanoticiasNOOdio=os.getcwd()+"\\NoOdio"
#RutanoticiasUnlabel=os.getcwd()+"\\Unlabeled"

#seleccionar elementos entrenamiento

LnoticiasOdioEntreno=Label(p1,text='Noticias Odio:')
LnoticiasOdioEntreno.place(relx=0.1,rely=0.1 , anchor=CENTER)

LnoticiasNoOdioEntreno=Label(p1,text='Noticias No Odio:')
LnoticiasNoOdioEntreno.place(relx=0.1,rely=0.2 , anchor=CENTER)

RutanoticiasOdiolabel = StringVar()
LnoticiasOdioEntrenoruta=Entry(p1,text='Ruta',width = 60, textvariable=RutanoticiasOdiolabel)
LnoticiasOdioEntrenoruta.place(height=19,relx=0.5,rely=0.1,anchor=CENTER)


BnoticiasOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:[carpeta(LnoticiasOdioEntrenoruta), vistaPrevia(RutanoticiasOdiolabel.get(),RutanoticiasNOOdiolabel.get(),variablealgoritmo)])
BnoticiasOdioEntrenoruta.place(relx=0.9,rely=0.1,anchor=CENTER)


RutanoticiasNOOdiolabel = StringVar()
LnoticiasNoOdioEntrenoboton=Entry(p1,text='Ruta',width = 60, textvariable=RutanoticiasNOOdiolabel)
LnoticiasNoOdioEntrenoboton.place(height=19,relx=0.5,rely=0.2,anchor=CENTER)

BnoticiasNoOdioEntrenoruta=Button(p1,text="Abrir",command=lambda:[carpeta(LnoticiasNoOdioEntrenoboton), vistaPrevia(RutanoticiasOdiolabel.get(),RutanoticiasNOOdiolabel.get(),variablealgoritmo)])
BnoticiasNoOdioEntrenoruta.place(relx=0.9,rely=0.2,anchor=CENTER)


#barra algoritmos
OptionList = [
"Decision Tree",
"SVM",
"Naive Bayes",

] 

variablealgoritmo = tk.StringVar(p1)
variablealgoritmo.set(OptionList[1])
clasificadorGlobal = variablealgoritmo.get()


opt = tk.OptionMenu(p1, variablealgoritmo, *OptionList, command = OptionMenu_SelectionEvent)
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


informacionalgoritmo2=Frame(p2)
informacionalgoritmo2.config(width=200,height=260,background="white",relief=tk.FLAT,bd=20,highlightthickness=4) 
informacionalgoritmo2.place(relx=0.82,rely=0.6,anchor=CENTER)


Linfo=Label(informacionalgoritmo2,text="RESUMEN:",font=('Arial',9)).place(relx=0.1,rely=0,anchor=CENTER)
Linfo1=Label(informacionalgoritmo2,text="Total noticias:",font=('Arial',7)).place(relx=0.1,rely=0.2,anchor=W)
Linfo2=Label(informacionalgoritmo2,text="Odio:",font=('Arial',7)).place(relx=0.1,rely=0.35,anchor=W)
Linfo3=Label(informacionalgoritmo2,text="NoOdio:",font=('Arial',7)).place(relx=0.1,rely=0.5,anchor=W)


Bseleccionarmodeloclasificador=Button(p2,text="Modelo",command=lambda:abrirarchivo(Lclasificador,Rutanoticiasclasificar.get(),tablita),state=tk.DISABLED)
Bseleccionarmodeloclasificador.place(relx=0.9,rely=0.2,anchor=CENTER)


Lguardarcsv=Label(p2,text="Guardar csv:").place(relx=0.1,rely=0.9)



Rdirguardartest = StringVar()
Lguardardirtest=Entry(p2,text='Ruta',width = 60, textvariable=Rdirguardar)
Lguardardirtest.place(height=19,relx=0.5,rely=0.925,anchor=CENTER)

BGuardarmodelo=Button(p2,text="Guardar",command=lambda:guardartest(Lguardardirtest,GuardCSV))
BGuardarmodelo.place(relx=0.9,rely=0.925,anchor=CENTER)

#Linfo4=Label(informacionalgoritmo2,text="Algoritmo seleccionado:",font=('Arial',7)).place(relx=0.1,rely=0.8,anchor=W)




#agregamos pestañas


nb.add(p1,text='entrenamiento')
nb.add(p2,text='clasificacion')



root.mainloop()

#fin interfaz


