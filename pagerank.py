import numpy as np

filepath = 'large-graph.txt'
matriceAdjacence = []
matriceTransition = []
probLambda = 0.85
prec = 0.0001

with open(filepath) as fp:  
	line = fp.readline()
	taille = int(line.strip())
	line = fp.readline()
	cnt = 0
	while line:
		list_line = [0]*taille
		tmp_list = line.strip().split(" ")
		for i in range(1, len(tmp_list)):
			list_line[int(tmp_list[i])] = 1
				
		matriceAdjacence.append(list_line)
		line = fp.readline()
		cnt += 1

	for i in range(taille) :
		list_line = [0]*taille
		for j in range(taille) :
			sumadj = sum(matriceAdjacence[i])
			tmpres = 0
			if sumadj > 0 :
				tmpres = (probLambda * (matriceAdjacence[i][j]/float(sumadj))) + ((1.0 - probLambda) * (1.0/float(taille)))
			else :
				tmpres = 1.0/float(taille)
			list_line[j] = tmpres
		matriceTransition.append(list_line)
	print matriceTransition


	pagerank = np.array([1.0/float(taille)] * taille)
	arrayTransition = np.array(matriceTransition)	
	l = 0

	pageranktmp = pagerank
	pagerank = pagerank.dot(arrayTransition)	
	while np.linalg.norm(pagerank - pageranktmp) > prec:
		pageranktmp = pagerank
		pagerank = pagerank.dot(arrayTransition)
		l+= 1
			
	print pagerank
	print("Stabilite en ",l,"etapes")
	print("Affichage du pagerank (tri par pagerank decroissant): ", list(reversed(pagerank.argsort())))

#Question 1)
#
#	Plus le critère d'arret est restrictif (petit), plus il faut d'itérations afin d'arriver à stabilité
#Question 2) 
#	Les autorités sont mieux classées
#Question 3)
#	Pour accroître le pagerank d'une page, il suffit d'ajouter des transitions vers cette page dans différents noeuds du graphe
#	Exemple avec le graphe suivant :
#6
#0 2 3
#1 0 3 5
#2 1 3 4 5
#3 0
#4 3
#5 2 3
#	Si on souhaite accroitre le rang de la page 4, on peut ajouter la valeur 4 à la ligne des noeuds 0 1 3 et 5. Si on fait ca, la page 4 aura le meilleur pagerank	
#Question 4)
#	Lorsque Lambda tend vers 0, les valeurs du vecteur du pagerank ont tendance à s'uniformiser (même valeur)
#

	
	
