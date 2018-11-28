# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:02:45 2018

@author: tomastom
"""

import pandas as pd
import copy
import numpy  as np
import networkx as nx
from scipy import optimize

import matplotlib.pylab as plt
#%%
nodos = pd.read_csv("nodes.csv",sep=";",error_bad_lines=False)
#%%
enlaces=pd.read_csv("edges.csv",sep=";",error_bad_lines=False)

#%% División antes, durante y después de la sesión
E=list(enlaces.Time.values) ##Me extrae los valores del tiempo
i1=E.index("2018-06-13 11:25:00") ##índice que nos dice cuando arranca la sesión
i2=E.index("2018-06-14 09:36:00") ##índice que nos dice cuando finaliza la sesión

E_antes=enlaces[:i1]
E_durante=enlaces[i1:i2]
E_despues=enlaces[i2:]
#%% Para pasarle a networkx
Enlaces_antes=[]
for i in range(len(E_antes)):
    Enlaces_antes.append((E_antes["Source"][i],E_antes["Target"][i]))

G_en_antes=nx.DiGraph()
G_en_antes.add_edges_from(set(Enlaces_antes))
#%%
G_en_antes_ND=nx.Graph()
G_en_antes_ND.add_edges_from(set(Enlaces_antes))
Gcc = sorted(nx.connected_component_subgraphs(G_en_antes_ND), key=len, reverse=True)
EnlaCompGigante=[] ##lista de enlaces que contiene la componente gigante. Son 10 mil menos que en la dirigida
for i in Gcc[0].edges:
    EnlaCompGigante.append(i)
#%%Grafo dirigido con los enlaces de la componente gigante
G_en_antes_PODADA=nx.DiGraph()
G_en_antes_PODADA.add_edges_from(EnlaCompGigante)
#%%Les damos el in_degree a los nodos
k_in=[]
k_out=[]
for i in G_en_antes.nodes():
    k_in.append(G_en_antes.in_degree(i)) ##Grado in
    k_out.append(G_en_antes.out_degree(i))
K_in=np.histogram(k_in,bins=10000)
K_out=np.histogram(k_out,bins=10000)
#%%Grafico la distribución de grado

plt.scatter(K_in[1][1:],K_in[0], label="K in")
plt.scatter(K_out[1][1:],K_out[0],label="K out",alpha=.5)
plt.xlabel("grado")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.ylim(0.5,10**5)
plt.xlim(1,10**4)
plt.show()
#%%Bineo logarítmico
bink=14
b=[0]
for i in range(bink):
    b[i]=b[i-1]+2**i
    b.append(b[i])
B=[]                 ##Este es el que vamos a usar para dar el ancho de los bines
for i in range(bink):
    B.append(b[i])
sorted(k_in)      #Ordenamos la lista de los grados de los nodos de menor a mayor
PklogIn=[]       ## Creamos una lista a la que le vamos a agregar la cantidad de nodos en un bin, dividido el ancho del bin. Considerando el vector de bins B
for i in range(bink):
    a=0
    for k in k_in:
        
        if B[i]<=k<B[i+1]:
            a+=1
    PklogIn.append(a/2**(1+i))
    
plt.scatter(B,PklogIn, label="Bineo logarítmico")
plt.scatter(K_in[1][1:],K_in[0], label="Bineo lineal",alpha=.8)
plt.xscale('log')
plt.yscale('log')
plt.ylim(ymax=10**5.5,ymin=10**(-2))
plt.xlabel("Grado")
plt.legend()
#%%Ajuste lineal
def fiteadora(p,x):
    return p[0]+p[1]*x

def error(p,x,y):
    return fiteadora(p,x)-y
#%%
P_ini=[4,-2]
logx=[]
for i in B[:10]:
    logx.append(np.log10(i))
logy=[]
for i in PklogIn[:10]:
    logy.append(np.log10(i))

out= optimize.leastsq(error,P_ini,args=(np.array(logx), np.array(logy)),full_output=1)
pfinal = out[0]
covar = out[1]
p0err=np.sqrt( covar[0][0] )
p1err= np.sqrt( covar[1][1] )

pfinal

Y=[]    ##Tiene problemitas el jupyter
for i in logx:
    Y.append(pfinal[0]+pfinal[1]*i)
plt.plot(logx, logy, "ro", label="Data")
plt.plot(logx, Y, "k-", label="Ajuste")
plt.scatter(np.log10(K_in[1][2:]),np.log10(K_in[0][1:]), label="Bineo lineal")
plt.xlabel("Logaritmo del grado")
plt.legend()
plt.ylabel("Logaritmo del número de ocurrencias")
plt.title('Gráfico 7: Distribución de grado y su ajuste lineal ')
plt.text(0, -0, 'Coeficiente ppal = %5.2f +/- %5.2f' % (pfinal[1], p1err))
plt.text(0, -.5, 'Ordenada = %5.2f +/- %5.2f' % (pfinal[0], p0err))
plt.show()
#%%Matriz de adyacencia
M=nx.adjacency_matrix(G_en_antes) ##el type es scipy.sparse.csr.csr_matrix
#Nos podemos mover fácilmente por los vecinos out de un nodo
M.indices

#%%
#def NodoGrado(Grafo):
#    Nodos=[] #lista con grado-nodo
#    for n in Grafo.nodes():
#        Nodos.append([Grafo.in_degree(n),n])
#    sorted(Nodos)
#    return Nodos 

def K_max(Grafo,GradoNodoBase):
    
    K=[]
    if GradoNodoBase=="in":
        for n in NodoInGrado(Grafo):
            K.append(n[0])
    if GradoNodoBase=="out":
        for n in NodoOutGrado(Grafo):
            K.append(n[0])
    K_max=max(K)
    return K_max #devuelve el grado maximo de la red
#%%
#def k_vec_in_in(Grafo):
#    Grado_GradoPromVec=[]
#    for n in NodoGrado(Grafo): #NodoGrado devuelve lista con con grado-nodo ordenada de menor a mayor grado 
#        Vecinos=nx.all_neighbors(Grafo,n[1]) #me devuelve todos los vecinos del nodo n[1]
#        K=Grafo.in_degree(Vecinos)
#        k_vecinos=[]
#        for i in K:
#            k_vecinos.append(i[1])
#        if len(K)!=0: #si el nodo tiene vecinos 
#            k_vecinos_promedio=sum(k_vecinos)/len(K)
#        else:
#            k_vecinos_promedio=0 #si el nodo no tiene vecinos
#        Grado_GradoPromVec.append([n[0],k_vecinos_promedio]) #Grado_GradoPromVec es una lista de listas con el grado de un nodo y el promedio del grado de sus correspondientes vecinos 
#    k_nn=[]
#    k=[]
#    for i in range(1,K_max(Grafo)+1):
#        a=0
#        b=0
#        for n in Grado_GradoPromVec: #Grado_GradoPromVec tiene grado de un nodo Y el promedio del grado de sus vecinos 
#            if n[0]==i:
#                a+=1 #cuento el numero de nodos con un determinado grado k
#                b+=n[1] #sumo para nodos de un mismo k, el promedio del grado de sus vecinos 
#        if a!=0: #si existen nodos con el grado i (si a es distinto de cero)
#            k_nn.append(b/a) #tiene el promedio sobre todos los nodos de grado k del promedio del grado de los vecinos de cada nodo 
#            k.append(i) # i es grado, a cada i le corresponde un elemento de k_nn
#    return k,k_nn
#%%
#def k_vec_in_out(Grafo):
#    Grado_GradoPromVec=[]
#    for n in NodoGrado(Grafo): #NodoGrado devuelve lista con con grado-nodo ordenada de menor a mayor grado 
#        Vecinos=nx.all_neighbors(Grafo,n[1]) #me devuelve todos los vecinos del nodo n[1]
#        K=Grafo.out_degree(Vecinos)
#        k_vecinos=[]
#        for i in K:
#            k_vecinos.append(i[1])
#        if len(K)!=0: #si el nodo tiene vecinos 
#            k_vecinos_promedio=sum(k_vecinos)/len(K)
#        else:
#            k_vecinos_promedio=0 #si el nodo no tiene vecinos
#        Grado_GradoPromVec.append([n[0],k_vecinos_promedio]) #Grado_GradoPromVec es una lista de listas con el grado de un nodo y el promedio del grado de sus correspondientes vecinos 
#    k_nn=[]
#    k=[]
#    for i in range(1,K_max(Grafo)+1):
#        a=0
#        b=0
#        for n in Grado_GradoPromVec: #Grado_GradoPromVec tiene grado de un nodo Y el promedio del grado de sus vecinos 
#            if n[0]==i:
#                a+=1 #cuento el numero de nodos con un determinado grado k
#                b+=n[1] #sumo para nodos de un mismo k, el promedio del grado de sus vecinos 
#        if a!=0: #si existen nodos con el grado i (si a es distinto de cero)
#            k_nn.append(b/a) #tiene el promedio sobre todos los nodos de grado k del promedio del grado de los vecinos de cada nodo 
#            k.append(i) # i es grado, a cada i le corresponde un elemento de k_nn
#    return k,k_nn
#%%
#A=k_vec_in_in(G_en_antes)
#B=k_vec_in_in(G_en_antes)
#%%
def creartxt(lista1,lista2,NombreArchivo):         ##Lo único que hay que decirle es las dos listas a guardar. Se podrían guardar más, pero hace falta agregar un par de cosas
    with open(NombreArchivo,'w') as f:             ##Nombre de archivo hay que ponerlo entre comillas y punto txt. Es el nombre que queremos que tenga el archivo
        a=0
        for item in lista1:
            f.write("{}\t{}\n".format(item,lista2[a]))
            a+=1
#%%
#creartxt(A[0],A[1],"out_in.txt")
#creartxt(B[0],B[1],"out_out.txt")
#creartxt(C[0],C[1],"in_in.txt")
#creartxt(D[0],D[1],"in_out.txt")
#%%
plt.scatter(K[0],K[1])
plt.ylabel("Ocurrencia")
plt.xlabel("Grado in")
plt.title('Grado in de los vecinos')
plt.xscale('log')
plt.yscale('log')
plt.scatter(A[0],A[1])
plt.ylabel("$k_{nn}$(k)")
plt.xlabel("Grado in")
plt.title('Grado in de los vecinos')
plt.xscale('log')
plt.yscale('log')
plt.show()
plt.title('Grado out de los vecinos')
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k)")
plt.xlabel("Grado in")
plt.scatter(B[0],B[1])
plt.show()
#%%
#Prueba=[(1,2),(1,3),(4,1)]
#PRUEBA=nx.DiGraph()
#PRUEBA.add_edges_from(Prueba)
#%%
#Nodo con su in degree
def NodoInGrado(Grafo):
    Nodos=[] #lista con grado-nodo
    for n in Grafo.nodes():
        Nodos.append([Grafo.in_degree(n),n])
    sorted(Nodos)
    return Nodos
#Nodo con su out degree
def NodoOutGrado(Grafo):
    Nodos=[] #lista con grado-nodo
    for n in Grafo.nodes():
        Nodos.append([Grafo.out_degree(n),n])
    sorted(Nodos)
    return Nodos

#%%
#Hagamos el que ve los vecinos out. Calculando en grado in de los vecinos. Partiendo del grado out
def k_vec(Grafo,GradoNodoBase,GradoVecino):
    Grado_GradoPromVec=[]
    M=nx.adjacency_matrix(Grafo)
    numnodo=0
    if GradoNodoBase=="out":
        NG=NodoOutGrado(Grafo)
    if GradoNodoBase=="in":
        NG=NodoInGrado(Grafo)
    if GradoVecino=="in":
        for n in NG:
            Vecinos=M[numnodo].indices ##array con los nodos vecinos out de numnodo
            Vecinos_label=[]
            for i in Vecinos:
                Vecinos_label.append(NG[i][1])
            K=Grafo.in_degree(Vecinos_label)
            k_vecinos=[]
            for i in K:
                k_vecinos.append(i[1])
            if len(K)!=0: #si el nodo tiene vecinos 
                k_vecinos_promedio=sum(k_vecinos)/len(K)
            else:
                k_vecinos_promedio=0 #si el nodo no tiene vecinos
            Grado_GradoPromVec.append([n[0],k_vecinos_promedio])
            numnodo+=1
    if GradoVecino=="out":
        for n in NG:
            Vecinos=M[numnodo].indices ##array con los nodos vecinos out de numnodo
            Vecinos_label=[]
            for i in Vecinos:
                Vecinos_label.append(NG[i][1])
            K=Grafo.out_degree(Vecinos_label)
            k_vecinos=[]
            for i in K:
                k_vecinos.append(i[1])
            if len(K)!=0: #si el nodo tiene vecinos 
                k_vecinos_promedio=sum(k_vecinos)/len(K)
            else:
                k_vecinos_promedio=0 #si el nodo no tiene vecinos
            Grado_GradoPromVec.append([n[0],k_vecinos_promedio])
            numnodo+=1
    k_nn=[]
    k=[]
    for i in range(1,K_max(Grafo,GradoNodoBase)+1):
        a=0
        b=0
        for n in Grado_GradoPromVec: #Grado_GradoPromVec tiene grado de un nodo Y el promedio del grado de sus vecinos 
            if n[0]==i:
                a+=1 #cuento el numero de nodos con un determinado grado k
                b+=n[1] #sumo para nodos de un mismo k, el promedio del grado de sus vecinos 
        if a!=0: #si existen nodos con el grado i (si a es distinto de cero)
            k_nn.append(b/a) #tiene el promedio sobre todos los nodos de grado k del promedio del grado de los vecinos de cada nodo 
            k.append(i) # i es grado, a cada i le corresponde un elemento de k_nn
    return k,k_nn