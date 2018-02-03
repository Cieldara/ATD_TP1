import sys
from random import randint

args = sys.argv[1:]
file = open(args[0],"w")
taille = int(args[1])
file.write(str(taille)+'\n') 
for i in range(0,taille):
	toWrite = str(i) + " "
	possibleDest = range(0,taille)
	possibleDest.remove(i)
	#Definition d'un seuil pour chaque noeud du graphe
	seuil = randint(0,taille)
	for j in possibleDest:
		value = randint(0,taille)
		if value <= seuil:
			toWrite += str(j) + " " 
	file.write(toWrite+'\n')
