import sys
import random
from decimal import Decimal
import operator

INF = Decimal(9999999999999999999999999999999999)
k = int(sys.argv[2])


def dist(p1, p2):
	return (Decimal(p1[0])-Decimal(p2[0]))**Decimal(2) + (Decimal(p1[1])-Decimal(p2[1]))**Decimal(2)

def kmeans(data, centroid, iterations):
	cluster = {}
	clusterSize = {}
	newCentroids = []

	for x in range(k):
		clusterSize[str(x)] = Decimal(0);
		newCentroids.append([Decimal(0),Decimal(0)])

	for x in data:
		menor = INF
		# print(data[x][0])
		for y in range(k):
			menorAux = dist(data[x], centroid[y]);
			if(menorAux < menor):
				menor = menorAux
				cluster[x] = y
		clusterSize[str(cluster[x])] += Decimal(1)


	for y in range(k):
		for x in cluster:
			if(cluster[x] == y):
				newCentroids[y][0] += Decimal(data[x][0])
				newCentroids[y][1] += Decimal(data[x][1])


	for x in range(k):
		newCentroids[x][0] = newCentroids[x][0]/clusterSize[str(x)]
		newCentroids[x][1] = newCentroids[x][1]/clusterSize[str(x)]


	if(iterations+1 < int(sys.argv[3])):
		return kmeans(data, newCentroids, iterations+1)
	else:
		print centroid
		return cluster


def main():
	centroid = []
	data = {}

	with open(sys.argv[1]) as fp:  
		line = fp.readline()
		line = fp.readline()
		clin = 1
		while line:
			clin += 1
			data[(line.split('	'))[0]] = line.replace('\n', '').split('	')[1:]
			line = fp.readline()

	for i in range(k):
		centroid.append(data.values()[random.randint(1, clin-1)])


	cluster = kmeans(data, centroid, 0)

	cluster = sorted(cluster.items(), key=operator.itemgetter(1))

	with open(sys.argv[1][:-4] + ".clu", "w") as fp:
		for x in cluster:
			# print(x + "	" + str(cluster[x]))
			fp.write(x[0] + "	" + str(x[1]) + "\n")
	# print data
	# print centroid

if __name__ == "__main__":
    main()