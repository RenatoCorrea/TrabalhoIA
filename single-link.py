import sys
import random
from decimal import Decimal
import operator

labelDic = {}
k_min = 0
k_max = 0
INF = 9999999999999
ncluster = "ncluster"

def dist(p1, p2):
	return (float(p1[0])-float(p2[0]))**float(2) + (float(p1[1])-float(p2[1]))**float(2)

def cDistMatrix(data):
	l = len(data)
	distMatrix = [[0 for x in range(l)] for y in range(l)]
	for i in range(l):
		for j in range(i, l):
			distMatrix[i][j] = dist(data[labelDic[i]][0], data[labelDic[j]][0])
			distMatrix[j][i] = distMatrix[i][j]
	return distMatrix


def min(i, j):
	if(i < j):
		return i
	return j

def max(i, j):
	if(i > j):
		return i
	return j


def singleLink(distMatrix, cluster, data):
	l = len(distMatrix[0])
	while(cluster[ncluster] >= k_min):
		print cluster[ncluster]
		menor = INF
		menorLabel = [0, 0]
		for n in range(l):#for in range(len(distList))
			# "distancia": [i, j]
			#adapta os id dentro da lista pra i e j nos campos abaixo
			# i = n[1][0]
			# j = n[1][1]
			novo = min(data[labelDic[i]][1], data[labelDic[j]][1])
			velho = max(data[labelDic[i]][1], data[labelDic[j]][1])
			# Lembrando que 'data' esta estruturado como:
			#	"label": [[d1, d2], clusterId]
			for s in cluster[velho]:
				cluster[novo].append(s)
				data[s][1] = novo 
			cluster[velho].clear()
			#cluster[ncluster] mantem o numero atual de clusters
			cluster[ncluster] -= 1

			if(cluster[ncluster] <= k_max):
				with open(sys.argv[1][:-4] + str(cluster[ncluster]) + ".clu", "w") as fp:
					for x in data:
						# print(x + "	" + str(cluster[x]))
						fp.write(x[0] + "	" + str(x[2]) + "\n")


# sigle-link.py file k_min k_max

def main():
	
	data = {}
	cluster = {}
	cluster[ncluster] = 0;
	k_min = sys.argv[2]
	k_max = sys.argv[3]

	with open(sys.argv[1]) as fp:
		line = fp.readline()
		line = fp.readline()
		clin = 1
		while line:
			label = (line.split('	'))[0]
			data[label] = [line.replace('\n', '').split('	')[1:]]
			data[label].append(clin)
			cluster[clin] = []
			cluster[clin].append(label)
			labelDic[clin-1] = label
			line = fp.readline()
			clin += 1

	cluster[ncluster] = clin - 1

	distMatrix = cDistMatrix(data)
	distList = []
	for i in range(l):
		for j in range(i, l):
			#Dic que guarda Distancia e ids i e j
			noAtual = {}
			noAtual[distMatrix[i][j]] = [i, j]
			distList
			#Criar lista de distancias 
	#ordenar lista de distancias
	singleLink(distMatrix, cluster, data)

if __name__ == "__main__":
    main()