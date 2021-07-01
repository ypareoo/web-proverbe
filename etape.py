# Créé par P. Bosseboeuf, le 07/04/2021 en Python 3.7
import random as random

compteur=0
proverbes=[]
ligne = "n'importe quoi"
with open("proverbes-UTF8.txt") as f: #compte le nombre de ligne du fichier
    while ligne!="" :
        ligne = f.readline()
        compteur+=1



with open("proverbes-UTF8.txt","r",encoding="utf-8") as f: #remplie un tableau avec l'ensemble des citation et attribution d'un numéro
    for line in range(compteur-1):
        proverbes.append(f.readline()[:-1]+" (citation n° "+str(line+1)+")")
#print(proverbes)

alea=random.randint(0,compteur-1) #génere un nbr aléatoire/ligne de code de test
#print(proverbes[alea])