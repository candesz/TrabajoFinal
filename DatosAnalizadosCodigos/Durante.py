# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:45:14 2018

@author: Pachy
"""
import numpy as np
##Durante
Enlaces_durante=[]
ELD=np.arange(i1,i2,1)
for i in ELD:
    Enlaces_durante.append((E_durante["Source"][i],E_durante["Target"][i]))

G_en_durante=nx.DiGraph()
G_en_durante.add_edges_from(set(Enlaces_durante))
#%%
k_in=[]
k_out=[]
for i in G_en_durante.nodes():
    k_in.append(G_en_durante.in_degree(i)) ##Grado in
    k_out.append(G_en_durante.out_degree(i))
K_in=np.histogram(k_in,bins=10000)
K_out=np.histogram(k_out,bins=10000)

#creartxt(K_in[1][1:],K_in[0],"K_inDurante.txt")
#creartxt(K_out[1][1:],K_out[0],"K_outDurante.txt")
#%%Grafico la distribución de grado
plt.scatter(K_in[1][1:],K_in[0], label="K in")
plt.scatter(K_out[1][1:],K_out[0],label="K out",alpha=.5)
plt.xlabel("grado")
plt.title("Distribución de grado Durante el Debate")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.ylim(0.5,10**5)
plt.xlim(1,10**5)
#%%
A=k_vec(G_en_durante,"in","in")
creartxt(A[0],A[1],"in_in.txt")
B=k_vec(G_en_durante,"in","out")
creartxt(B[0],B[1],"in_out.txt")

C=k_vec(G_en_durante,"out","in")
creartxt(C[0],C[1],"out_in.txt")
D=k_vec(G_en_durante,"out","out")
creartxt(D[0],D[1],"out_out.txt")
#%%
plt.scatter(A[0],A[1])
plt.ylabel("$k_{nn}$(k) con grado in")
plt.xlabel("Grado out")
plt.xscale('log')
plt.yscale('log')
plt.xlim(.5,25000)
plt.ylim(.5,30000)
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k) con grado out")
plt.xlabel("Grado out")
plt.scatter(B[0],B[1])
plt.xlim(.5,20000)
plt.ylim(.2,100)
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k) con grado in")
plt.xlabel("Grado in")
plt.scatter(C[0],C[1])
plt.xlim(.5,800)
plt.ylim(5,8000)
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k) con grado out")
plt.xlabel("Grado in")
plt.scatter(D[0],D[1])
plt.xlim(.5,1200)
plt.ylim(4,15)
plt.show()