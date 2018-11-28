# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:10:20 2018

@author: Pachy
"""

import matplotlib.pylab as plt
import numpy as np
import scipy as sp

def leetxt(NombreArchivo):    ##Le ponés entre comillas y .txt el nombre del archivo y lo lee
    lectura1=[]               ##la función devuelve dos listas. la primera es la lista1 de arriba, la segunda la lista2
    lectura2=[]               ##Para aplicarla es poner f=leetxt("NombreArchivo.txt")
    with open(NombreArchivo, 'r') as f: ## f[0] va a ser lista1
        contenido= f.readlines()        ## f[1] va a ser lista2
        for x in contenido:             ## Al igual que la de arriba se puede extender fácil a más de dos listas
            row = x.split()
            lectura1.append(float(row[0]))
            lectura2.append(float(row[1]))
    return lectura1, lectura2

#%%
A_antes=leetxt("ANTES\out_in.txt")
A_durante=leetxt("DURANTE\out_in.txt")
#%%
plt.scatter(A_antes[0],A_antes[1],label="Antes")
plt.scatter(A_durante[0],A_durante[1],label="Durante")
plt.ylabel("$k_{nn}$(k) con grado in")
plt.xlabel("Grado in")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlim(.5,50000)
plt.ylim(.3,40000)
plt.show()
#%%
B_antes=leetxt("ANTES\out_out.txt")
B_durante=leetxt("DURANTE\out_out.txt")
#%%
plt.scatter(B_antes[0],B_antes[1],label="Antes")
plt.scatter(B_durante[0],B_durante[1],label="Durante")
plt.ylabel("$k_{nn}$(k) con grado out")
plt.xlabel("Grado in")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlim(.5,50000)
plt.ylim(.2,100)
plt.show()