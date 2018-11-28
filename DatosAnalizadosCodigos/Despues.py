# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:31:37 2018

@author: Pachy
"""

Enlaces_despues=[]
ELD=np.arange(i2,2151030,1)
for i in ELD:
    Enlaces_despues.append((E_despues["Source"][i],E_despues["Target"][i]))

G_en_despues=nx.DiGraph()
G_en_despues.add_edges_from(set(Enlaces_despues))
#%%
def K(H,direccion):
    if direccion=="in":
        k=sum(H.in_degree(k) for k in H)/H.number_of_nodes()
    if direccion=="out":
        k=sum(H.out_degree(k) for k in H)/H.number_of_nodes()
    salida=[k]
    return salida
#%%
k_in=[]
k_out=[]
for i in G_en_despues.nodes():
    k_in.append(G_en_despues.in_degree(i)) ##Grado in
    k_out.append(G_en_despues.out_degree(i))
K_in=np.histogram(k_in,bins=10000)
K_out=np.histogram(k_out,bins=10000)

#creartxt(K_in[1][1:],K_in[0],"K_inDespues.txt")
#creartxt(K_out[1][1:],K_out[0],"K_outDespues.txt")
#%%Grafico la distribución de grado
plt.scatter(K_in[1][1:],K_in[0], label="K in",alpha=.8)
plt.scatter(K_out[1][1:],K_out[0],label="K out",alpha=.8)
plt.xlabel("grado")
plt.title("Distribución de grado Después del Debate")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.ylim(0.5,10**5)
plt.xlim(1,10**5)
#%%
A=k_vec(G_en_despues,"in","in")
creartxt(A[0],A[1],"in_in.txt")
B=k_vec(G_en_despues,"in","out")
creartxt(B[0],B[1],"in_out.txt")

C=k_vec(G_en_despues,"out","in")
creartxt(C[0],C[1],"out_in.txt")
D=k_vec(G_en_despues,"out","out")
creartxt(D[0],D[1],"out_out.txt")

#%%
plt.scatter(A[0],A[1])
plt.ylabel("$k_{nn}$(k) con grado in")
plt.xlabel("Grado in")
plt.xscale('log')
plt.yscale('log')
plt.xlim(.5,25000)
plt.ylim(.5,30000)
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k) con grado out")
plt.xlabel("Grado in")
plt.scatter(B[0],B[1])
plt.xlim(.5,25000)
plt.ylim(.09,20)
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k) con grado in")
plt.xlabel("Grado out")
plt.scatter(C[0],C[1])
plt.xlim(.5,200)
plt.ylim(10,2000)
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.ylabel("$k_{nn}$(k) con grado out")
plt.xlabel("Grado out")
plt.scatter(D[0],D[1])
plt.xlim(.5,200)
plt.ylim(.5,8)
plt.show()