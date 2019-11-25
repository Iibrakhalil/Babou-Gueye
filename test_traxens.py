import numpy as np
import random
from random import randint
from time import strftime, gmtime
from scipy import append


id_porte = np.arange(1, 201, 1) #numeros des portes
################################ simulation des evenements, 1=evenmnt(porte ouverte), 0=fermée
etat_porte = []         
for i in range(1000):
    etat_porte.append( randint(0,1) )
etat_porte
############################# simulation des portes
porte = []                           
for i in range(1000):
    porte.append( randint(1,200) )
porte
##############
heure = []
for i in range(1000):
    heure.append(randint(1,86400))
heure
############################################## simulation des heures
Heur=[]
for i in range(1000):
    Heur.append(strftime('%H %M %S', gmtime((randint(1,86400)))))
Heur.sort()
Heur
len(Heur)
######################################### creation jeu de donnees
donnee = append(porte, etat_porte).T
donnees = append(donnee,Heur)
M=donnees.reshape(1000,3)

#a= np.savetxt("donnees",M, delimiter="\t")
