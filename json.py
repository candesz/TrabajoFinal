# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:24:43 2018

@author: cande
"""
import networkx as nx
import json
import copy
from networkx.algorithms import community
from networkx.algorithms.community import greedy_modularity_communities
#%%
with open('tweets_aborto.json', 'r') as infile:

    # Variable for building our JSON block
    json_block = []

    for line in infile:
        if line.startswith('{"limit"') or line.startswith('\n'):
            pass
        else:
        # Add the line to our JSON block
            json_block.append(line)

        # Check whether we closed our JSON block
        if line.startswith('}'):

            # Do something with the JSON dictionary
            json_dict = json.loads(''.join(json_block))
            print(json_dict)

            # Start a new block
            json_block = []
                
#%%
#Múltiplos de tres son tweets

#json.loads(json_block[3])
#dic=json.loads(json_block[3])
#dic["text"] #Devuelve el texto
#dic["user"]["screen_name"]

#List=[]
#for i in range(len(json_block)): #Versión lenta
 #   d=json.loads(json_block[i])
  #  if keys[2] in d:
   #     dict={x:d[x] for x in keys}
    #    List.append(dict)
    #else:
     #   pass
 #%%    
RT=[]    
for i in json_block: #Versión rápida
    if('retweeted_status' in i)==True:
       RT.append(i)
       
Aborto=[]
Otro_tema=[]
for i in range(len(RT)):
    if 'aborto' in RT[i]:
        Aborto.append(RT[i])
    else:
        if 'Aborto' in RT[i]:
            Aborto.append(RT[i])
        else:
            if 'ProVida' in RT[i]:
                Aborto.append(RT[i])
            else:
                if 'SiALaVida' in RT[i]:
                    Aborto.append(RT[i])
                else:
                    if 'ABORTO' in RT[i]:
                        Aborto.append(RT[i])
                    else:
                        if 'AbortoLegalYa' in RT[i]:
                            Aborto.append(RT[i])
                        else:
                            if 'AbortoLegalOClandestino' in RT[i]:
                                Aborto.append(RT[i])
                            else:
                                if 'SalvemosLas2Vidas' in RT[i]:
                                    Aborto.append(RT[i])
                                else:
                                    if 'MentiraVerde' in RT[i]:
                                        Aborto.append(RT[i])
                                    else:
                                        if 'ArgentinaEsProvida' in RT[i]:
                                            Aborto.append(RT[i])                                           
                                        else:
                                            if 'ESprovida' in RT[i]:
                                                Aborto.append(RT[i])
                                            else:
                                                if "AbortoSesiónHistórica" in RT[i]:
                                                    Aborto.append(RT[i])
                                                else:
                                                    if 'SalvemosLasDosVidas' in RT[i]:
                                                        Aborto.append(RT[i])
                                                    else:
                                                        if "QueSeaLey" in RT[i]:
                                                            Aborto.append(RT[i])
                                                        else:
                                                            if 'provida' in RT[i]:
                                                                Aborto.append(RT[i])
                                                            else:
                                                                Otro_tema.append(RT[i])
#%%       
#keys=['created_at','text','user','retweeted_status']
                                                            
Lista=[] #Lista de diccionarios
for i in Aborto:
    D=json.loads(i)
    dict={'fecha':D['created_at'],"text":D["text"], "username":D["user"],"usuariore":D["retweeted_status"]["user"]}
    if ("extended_tweet" in D["retweeted_status"])==True:
        dict["extended_tweet"]=D["retweeted_status"]["extended_tweet"]['full_text']
    else:
        dict["extended_tweet"]="null"
    Lista.append(dict)
#%%    
#Filtrar por tema #aborto: DONE
# día DONE
# generar lista de enlaces.     DONE 
#Atributos? A favor o en contra?   CHECK
Martes12=[]
Mier13=[]
for i in Lista:
    if 'Jun 12' in i['fecha']:
        Martes12.append(i)
    else:
        if 'Jun 13' in i['fecha']:
            Mier13.append(i)
        else:
            pass
#%%        
Id=[]
Name=[]
for i in range(len(Lista)):
    Id.append(Lista[i]['username']['id_str'])
    Name.append(Lista[i]['username']['screen_name'])
dict={}
for i in range(len(Id)):
    dict[Id[i]]=Name[i]
#%%    
Text=[]
for i in Lista:
    if 'AbortoLegalYa' in i['text']:
        Text.append('Verde')
    else:
        if 'SiALaVida' in i['text']: 
            Text.append('Celeste')
        else:
            if 'Provida' in i['text']:
                Text.append('Celeste')
            else:
                if 'SalvemosLas2Vidas' in i['text']:
                    Text.append('Celeste')
                else:
                    if 'AbortoLegalOCladenstino' in i['text']:
                        Text.append('Verde')
                    else:
                        if 'MentiraVerde' in i['text']:
                            Text.append('Celeste')
                        else:
                            if 'ArgentinaEsProvida' in i['text']:
                                Text.append('Celeste')
                            else:
                                if 'SeraLey' in i['text']:
                                    Text.append('Verde')
                                else:
                                    if 'legal seguro' in i['text']:
                                        Text.append('Verde')
                                    else:
                                        if 'pro vida' in i['text']:
                                            Text.append('Celeste')
                                        else:
                                            Text.append('A definir')
a=0
v=0
c=0
for i in Text:
    if i=='A definir':
        a+=1  
    if i=='Verde':        
        v+=1
    if  i=='Celeste':
        c+=1
#%%        
dict2={}
for i in range(len(Id)):
    dict2[Id[i]]=Text[i]
#%%    
Id2=[]    
Name2=[]
for i in range(len(Lista)):
    Id2.append(Lista[i]['usuariore']['id_str'])
    Name2.append(Lista[i]['usuariore']['screen_name'])
dictRT={}
for i in range(len(Id2)):
    dictRT[Id2[i]]=Name2[i]
#%%    
Pos=[]      
Palabras=["AgustinLaje","NadieMenos","AbortoNoESNiUnaMenos","ABORTONOESNIUNAMENOS","ArgentinaDefiendeLas2Vidas",'SalvemosLas2Vidas','SalvemosLasDosVidas','SiALaVida','ArgentinaEsProvida','MentiraVerde',"ArgentinaDefiendeLaVida",'AbortoLegalYa',"AbortoLegalSeguroGratuito ",'AbortoLegalOCladenstino','SeraLey',"SeVaACaer","QueSeaLey","NiUnaMenos","antiderecho", "legal seguro", "Aborto legal", "ABORTO LEGAL SEGURO Y GRATUITO"]
Color=["c","c","c",'c','c','c','c','c','c','c','c','v','v','v','v','v','v','v','v','v','v','v']
for j in Lista:
    c=0
    v=0
    for i in range(len(Palabras)):
        if Color[i]=="c":
            if (Palabras[i] in j['text'])==True or (Palabras[i] in j['extended_tweet'])==True:
                c+=1
        else:
            if Color[i]=="v":
                if (Palabras[i] in j['text'])==True or (Palabras[i] in j['extended_tweet'])==True:
                    v+=1
        #print(c,v)
    if c>v:
        Pos.append("c")
    else:
        if v>c:
            Pos.append("v")
        else:
            Pos.append("a definir")
c=0
v=0
a=0
for i in Pos:
    if i=='a definir':
        a+=1  
    if i=='v':        
        v+=1
    if  i=='c':
        c+=1
#%%
#dic_pos={}
#for i in range(len(Id)):
 #   dic_pos[Id[i]]=Pos[i]        
#%%    
Enlace=[]
for i in Lista:
    Enlace.append([i['username']['id_str'],i['usuariore']['id_str']])
    
#%%
EnlaceMartes=[]
for i in Martes12:
    EnlaceMartes.append([i['username']['id_str'],i['usuariore']['id_str']]) 
    
EnlaceMier=[]
for i in Mier13:
    EnlaceMier.append([i['username']['id_str'],i['usuariore']['id_str']])
#%%
EnlacePos=[]
for i in range(len(Lista)):
    EnlacePos.append([Enlace[i][1],Enlace[i][0],Pos[i]])    #Retweeteado primero
    
#%%
UsuariosRT=[]
for i in  Lista:
    UsuariosRT.append(i['usuariore']['id_str'])
    
UsuariosIN=[]
for i in  Lista:
    UsuariosIN.append(i['username']['id_str'])

Uin=set(UsuariosIN)
Urt=set(UsuariosRT)
Repetidos=[]
for i in Uin:
    if (i in Urt)==True:
        Repetidos.append(i)
#%%
PosRT=[]      
Palabras=["AgustinLaje","NadieMenos","AbortoNoESNiUnaMenos","ABORTONOESNIUNAMENOS","ArgentinaDefiendeLas2Vidas",'SalvemosLas2Vidas','SalvemosLasDosVidas','SiALaVida','ArgentinaEsProvida','MentiraVerde',"ArgentinaDefiendeLaVida",'AbortoLegalYa',"AbortoLegalSeguroGratuito ",'AbortoLegalOCladenstino','SeraLey',"SeVaACaer","QueSeaLey","NiUnaMenos","antiderecho", "legal seguro", "Aborto legal", "ABORTO LEGAL SEGURO Y GRATUITO", "clandestino","malepichot", "empatia" ]
Color=["c","c","c",'c','c','c','c','c','c','c','c','v','v','v','v','v','v','v','v','v','v','v','v','v','v']
for j in Lista:
    c=0
    v=0
    for i in range(len(Palabras)):
        if Color[i]=="c":
            if (Palabras[i] in j['extended_tweet'])==True:
                c+=1
        else:
            if Color[i]=="v":
                if (Palabras[i] in j['extended_tweet'])==True:
                    v+=1
        #print(c,v)
    if c>v:
        PosRT.append("c")
    else:
        if v>c:
            PosRT.append("v")
        else:
            PosRT.append("a definir")
c=0
v=0
a=0
for i in PosRT:
    if i=='a definir':
        a+=1  
    if i=='v':        
        v+=1
    if  i=='c':
        c+=1        
#%% 
EnlacePosRT=[]
for i in range(len(Lista)):
    EnlacePosRT.append([Enlace[i][1],Enlace[i][0],PosRT[i]])
EnlacePosRT=sorted(EnlacePosRT)    
     
#%%      
RTpos=[]      #probar a+=1
for i in Urt:
    c=0
    v=0
    a=0
    for j in EnlacePosRT:
        if j[0]==i:
            a+=1
            if j[2]=='v':
                v+=1
            else:
                if j[2]=='c':
                    c+=1
                
        else:
            pass
    nulo=a-c-v
    RTpos.append([i,c,v,nulo])
        
    #if c==v:
     #  RTpos.append([i,'A definir'])
    #else:
     #   if max(c,v,nulo)==v and max(c,v,nulo)!=nulo:
      #      RTpos.append([i,'Verde'])
      #  else:
       #     if max(c,v,nulo)==c and max(c,v,nulo)!=nulo:
        #        RTpos.append([i,'Celeste'])
         #   else:
          #      RTpos.append([i,'A definir'])"
 
#%%   

PosIN=[]
for i in Uin: 
    c=0
    v=0
    a=0
   
    for j in EnlacePos:
        if j[1]==i:
            a+=1
            if j[2]=='c':
                c+=1
            else:
                if j[2]=='v':
                    v+=1
                
        else:
            pass
    nulo=a-c-v
    PosIN.append([i,c,v,nulo])        
   # if c==v:
    #    Posicion.append('A definir')
    #else:
     #   if max(c,v,nulo)==v and max(c,v,nulo)!=nulo:
      #      Posicion.append('Verde')
       # else:
        #    if max(c,v,nulo)==c and max(c,v,nulo)!=nulo:
         #       Posicion.append('Celeste')
          #  else:
           #     Posicion.append('A definir')
            
            
    #PosIN.append([i,Posicion[0]])  
#%%
Posicion_nodo=[]     
for i in RTpos:
    if i[0] in Repetidos:
        for  j in PosIN:
            if i[0]==j[0]:
                cin=i[1]
                crt=j[1]
                c=i[1]+j[1]
                v=i[2]+j[2]
                nulo=i[3]+j[3]
        if c==v:
            Posicion_nodo.append([i[0],'A definir'])
        else:
            if max(c,v,nulo)==v and max(c,v,nulo)!=nulo:
                Posicion_nodo.append([i[0],'Verde'])
            else:
                if max(c,v,nulo)==c and max(c,v,nulo)!=nulo:
                    Posicion_nodo.append([i[0],'Celeste'])
                else:
                    Posicion_nodo.append([i[0],'A definir'])
                

    else:
        if i[1]==i[2]:
            Posicion_nodo.append([i[0],'A definir'])
        else:
            if max(i[1],i[2],i[3])==i[2] and max(i[1],i[2],i[3])!=i[3]:
                Posicion_nodo.append([i[0],'Verde'])
            else:
                if max(i[1],i[2],i[3])==i[1] and max(i[1],i[2],i[3])!=i[3]:
                    Posicion_nodo.append([i[0],'Celeste'])
                else:
                    Posicion_nodo.append([i[0],'A definir']) 
                   
for l in PosIN:
    if (l[0] in Repetidos)==False:
        if l[1]==l[2]:
            Posicion_nodo.append([l[0],'A definir'])
        else:
            if max(l[1],l[2],l[3])==l[2] and max(l[1],l[2],l[3])!=l[3]:
                Posicion_nodo.append([l[0],'Verde'])
            else:
                if max(l[1],l[2],l[3])==l[1] and max(l[1],l[2],l[3])!=l[3]:
                    Posicion_nodo.append([l[0],'Celeste'])
                else:
                    Posicion_nodo.append([l[0],'A definir'])           
#%%                    
dic_posicion={}
for i in range(len(Posicion_nodo)):
    dic_posicion[Posicion_nodo[i][0]]=Posicion_nodo[i][1]
#%%    
G12=nx.DiGraph()
G12.add_edges_from(EnlaceMartes)
Grado_in={}
Grado_out={}
for nodes in G12.nodes():
   Grado_in[nodes]=G12.in_degree(nodes)
   Grado_out[nodes]=G12.out_degree(nodes)
   
#%%   
G13=nx.DiGraph()
G13.add_edges_from(EnlaceMier)
Grado_in={}
Grado_out={}
for nodes in G13.nodes():
   Grado_in[nodes]=G13.in_degree(nodes)
   Grado_out[nodes]=G13.out_degree(nodes)
      
#%%
Nodos_a_sacar=[]
for nodo in G12.nodes():
    if Grado_in[nodo]==0 and  Grado_out[nodo]==1:
        Nodos_a_sacar.append(nodo)
#%%
Nodos_a_sacar_mier=[]
for nodo in G13.nodes():
    if Grado_in[nodo]==0 and Grado_out[nodo]==1:
        Nodos_a_sacar_mier.append(nodo)        
#%%%    

GMar=copy.deepcopy(G12)         
GMar.remove_nodes_from(Nodos_a_sacar)
Gmar=GMar.to_undirected()
Gcc=sorted(nx.connected_component_subgraphs(Gmar),key=len, reverse=True) 
G0=Gcc[0]   
nx.write_gml(G0,'Martes.gml')
#%%
GMier=copy.deepcopy(G13)         
GMier.remove_nodes_from(Nodos_a_sacar_mier)
GM=GMier.to_undirected()
Gcc=sorted(nx.connected_component_subgraphs(GM),key=len, reverse=True) 
G0M=Gcc[0]
   
#nx.write_gml(G0M,'Mier.gml')
#%%


comus = nx.algorithms.community.greedy_modularity_communities(G0M, weight=None)
