import numpy as np

filepath = 'large-graph.txt'
matriceAdjacence = []
matriceTransition = []
probLambda = 0.85
prec = 0.00001

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
		#print("Line {}: {}".format(cnt, line.strip()))
		line = fp.readline()
		cnt += 1

	for i in range(taille) :
		list_line = [0]*taille
		for j in range(taille) :
			sumadj = sum(matriceAdjacence[i])
			tmpres = 0
			if sumadj != 0 :
				tmpres = (probLambda * (matriceAdjacence[i][j]/float(sumadj))) + ((1 - probLambda) * (1/float(taille)))
			else :
				tmpres = 1/float(taille)
			list_line[j] = tmpres
		matriceTransition.append(list_line)
		#print("Sum={}".format(sum(list_line)))
	print matriceTransition

	pagerank = np.array([1/float(taille)] * taille)
	arrayTransition = np.array(matriceTransition)	
	l = 0
	
	while True:
		pageranktmp = pagerank
		pagerank = pagerank.dot(arrayTransition)
		l+= 1
		if np.linalg.norm(pagerank - pageranktmp) <= prec:
			break
			
	print pagerank
	print("L={} norm={}".format(l, np.linalg.norm(pageranktmp - pagerank)))
	print("Affichage du pagerank : ", list(reversed(pagerank.argsort())))
	
	
