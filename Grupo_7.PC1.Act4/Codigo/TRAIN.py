# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:57 2022

@author: Yago
"""
#import os
from CreadorDF import CreadorDF

from sklearn.model_selection import train_test_split
#from sklearn import datasets
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
#from sklearn.metrics import accuracy_score
from sklearn import tree


class TRAIN:
    
    def dataFrameEntrenamiento(self, pathOdio, pathNoOdio):
        creador = CreadorDF()
        tablaTrain, palabras = creador.creadorDFTrain(pathOdio, pathNoOdio)
        return tablaTrain, palabras
    
    def EntrenarSVM(self, dfEntrenamiento):

        X = dfEntrenamiento.drop(columns="CATEGORIA")
        y = dfEntrenamiento.iloc[:, 0]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
        
        clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
        matriz = confusion_matrix(y_test, clf.predict(X_test))
        precision = clf.score(X_test, y_test)*100
        print("Matriz de confusion SVM:")
        print(matriz)
        print("Precision SVM: "+str(round(precision, 2))+"%")
        return clf, matriz, precision
    
    def EntrenarNaiveBayes(self, dfEntrenamiento):
        X = dfEntrenamiento.drop(columns="CATEGORIA")
        y = dfEntrenamiento.iloc[:, 0]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
        
        gnb = GaussianNB().fit(X_train, y_train)
        matriz = confusion_matrix(y_test, gnb.predict(X_test))
        precision = gnb.score(X_test, y_test)*100
        
        print("Matriz de confusion Naive Bayes:")
        print(matriz)
        print("Precision Naive Bayes: "+str(round(precision, 2))+"%")
        return gnb, matriz, precision
    
    def EntrenarDecisionTree(self, dfEntrenamiento):

        #elimina la columna categoria
        X = dfEntrenamiento.drop(columns="CATEGORIA")

        #guarda solo la categora
        y = dfEntrenamiento.iloc[:, 0]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
        
        clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
        matriz = confusion_matrix(y_test, clf.predict(X_test))
        precision = clf.score(X_test, y_test)*100
        
        print("Matriz de confusion Decision Tree:")
        print(matriz)
        print("Precision Decision Tree: "+str(round(precision, 2))+"%")
        return clf, matriz, precision
    
    def Train(self, pathOdio, pathNoOdio, algoritmo):
        #paths = [os.getcwd() + "\\Odio", os.getcwd() + "\\NoOdio", os.getcwd() + "\\Unlabeled"]
        dfEntrenamiento, listapalabras = self.dataFrameEntrenamiento(pathOdio, pathNoOdio)
        
        if algoritmo == "SVM":
            CLF, matrix, precision = self.EntrenarSVM(dfEntrenamiento)
        elif algoritmo == "Naive Bayes":
            CLF, matrix, precision = self.EntrenarNaiveBayes(dfEntrenamiento)
        elif algoritmo == "Decision Tree":
            CLF, matrix, precision = self.EntrenarDecisionTree(dfEntrenamiento)
    
        return CLF, matrix, precision, listapalabras
    #print(dfEntrenamiento)