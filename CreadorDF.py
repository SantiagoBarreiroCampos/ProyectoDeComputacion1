# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:49:12 2022

@author: Yago
"""

import pandas as pd
import os
#import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

class CreadorDF:
    
    def noticiasLower(self, arrayNoticias):
        noticiaslower = []
        for noticia in arrayNoticias:
            noticiaslower.append(noticia.lower())
        return noticiaslower
    
    def tokenize(self, arrayNoticias):
        noticiasTokenizadas = []
        tokenizer = RegexpTokenizer(r"[a-zA-ZáéíóúñÁÉÍÓÚÑ]+")
        for noticia in arrayNoticias:
            noticiasTokenizadas.append(tokenizer.tokenize(noticia))
        
        return noticiasTokenizadas
    
    def removeStopwords(self, noticia):
        with open("listaParadaEsp.txt") as f:
            text = f.read()
            prohibitedWords = text.split("\n")
            return [word for word in noticia if not word in prohibitedWords]
        
    def stemming(self, noticia):
        stemmer = SnowballStemmer(language="spanish")
        return ' '.join([stemmer.stem(word)for word in noticia])
    
    def creadorDFTest(self,pathUnlabeled):
        files = os.listdir(pathUnlabeled)
        arrayNoticias = []
        
        for file in files:
            file_path = os.path.join(pathUnlabeled, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding="ISO 8859-1") as f:
                    
                    fileread = f.read();
                    splitedcontent = fileread.split("\n#####\n")#0=link 1=autor 2=fecha 3=titulo 4=content
                    #juntar title y content
                    content=splitedcontent[3]+" "+splitedcontent[4]+" "+splitedcontent[5]
                    arrayNoticias.append(content)
                    
        arrayNoticias = self.noticiasLower(arrayNoticias)
        arrayNoticias = self.tokenize(arrayNoticias)
        
        noticiasSinStop = []
        for noticia in arrayNoticias:
            noticiasSinStop.append(self.removeStopwords(noticia))
        
        noticiasStem = []
        for noticia in noticiasSinStop:
            noticiasStem.append(self.stemming(noticia))
        #print(noticiasStem[0])
        
        vectorizer = TfidfVectorizer()
        vectorNoticias = vectorizer.fit_transform(noticiasStem)
        palabras = vectorizer.get_feature_names()
        array = vectorNoticias.toarray()
        
        tabla = pd.DataFrame(data = array, index = files, columns = palabras)
        '''
        index = tabla.index
        i=0;
        categorias = []
        for nombreArchivo in index:
            if "NoOdio" in nombreArchivo:
                categorias.append("NoOdio")
            else:
                categorias.append("Odio")
            i+=1 
        tabla.insert(0, "CATEGORIA", categorias, True)
        '''
        return tabla
    
    
    
    def creadorDFTrain(self,pathOdio, pathNoOdio):
        filesOdio = os.listdir(pathOdio)
        filesNoOdio = os.listdir(pathNoOdio)
        files = filesOdio+filesNoOdio
        arrayNoticias = []
        for file in filesOdio:
            file_path = os.path.join(pathOdio, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding="ISO 8859-1") as f:
                    
                    fileread = f.read();
                    splitedcontent = fileread.split("\n#####\n")#0=link 1=autor 2=fecha 3=titulo 4=content
                    #juntar title y content
                    content=splitedcontent[3]+" "+splitedcontent[4]+" "+splitedcontent[5]
                    arrayNoticias.append(content)
                    
        for file in filesNoOdio:
            file_path = os.path.join(pathNoOdio, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding="ISO 8859-1") as f:
                    
                    fileread = f.read();
                    splitedcontent = fileread.split("\n#####\n")#0=link 1=autor 2=fecha 3=titulo 4=content
                    #juntar title y content
                    content=splitedcontent[3]+" "+splitedcontent[4]+" "+splitedcontent[5]
                    arrayNoticias.append(content)
                    
        arrayNoticias = self.noticiasLower(arrayNoticias)
        arrayNoticias = self.tokenize(arrayNoticias)
        
        noticiasSinStop = []
        for noticia in arrayNoticias:
            noticiasSinStop.append(self.removeStopwords(noticia))
        
        noticiasStem = []
        for noticia in noticiasSinStop:
            noticiasStem.append(self.stemming(noticia))
        #print(noticiasStem[0])
        
        vectorizer = TfidfVectorizer()
        vectorNoticias = vectorizer.fit_transform(noticiasStem)
        palabras = vectorizer.get_feature_names()
        array = vectorNoticias.toarray()
        
        tabla = pd.DataFrame(data = array, index = files, columns = palabras)
        
        index = tabla.index
        i=0;
        categorias = []
        for nombreArchivo in index:
            if "NoOdio" in nombreArchivo:
                categorias.append("NoOdio")
            else:
                categorias.append("Odio")
            i+=1 
        tabla.insert(0, "CATEGORIA", categorias, True)
        
        return tabla, palabras
        
    '''
    def creador_init(self, path):
        #paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio"] #Categorias a revisar, mirar que esten asi en el periodico (url)
        tabla = self.creadorDF(path) #Tiene que ser en minuscula
        #print(tablaOdio)
        #tablaNoOdio = self.creadorDF(paths[1])
        return tabla
    '''
    

#json_final = scrapeo_init() #Tiene que ser en minuscula