from graph import *
from vertex import *
from dijkstra import *
from random import random
from random import choice
import time
import csv
import pandas as pd

#you need to install matplotlib to be able to plot
import matplotlib
import numpy as np #you need to install numpy package
import matplotlib.pyplot as plt

# graphs
costGraph = Graph()
distGraph = Graph()

# read data from dataset
df = pd.read_csv('./dataSets/cleaned.csv')

#Tracks index of vertice in graph
VertIndex = []

for idx, row in df.iterrows():
    if row[0] not in VertIndex:
        costGraph.addVertex(Vertex(row[0]))
        distGraph.addVertex(Vertex(row[0]))
        VertIndex.append(row[0])

    if row[1] not in VertIndex:
        costGraph.addVertex(Vertex(row[1]))
        distGraph.addVertex(Vertex(row[1]))
        VertIndex.append(row[1])


    costGraph.addDiEdge(costGraph.vertices[VertIndex.index(row[0])],costGraph.vertices[VertIndex.index(row[1])],row[2])
    distGraph.addDiEdge(distGraph.vertices[VertIndex.index(row[0])],distGraph.vertices[VertIndex.index(row[1])],row[3])

costOrg  = costGraph.vertices[VertIndex.index('SFB')]
distOrg  = distGraph.vertices[VertIndex.index('SFB')]
costDest = costGraph.vertices[VertIndex.index('YNG')]
distDest = distGraph.vertices[VertIndex.index('YNG')]

dijkstra(costOrg, costGraph)
dijkstra(distOrg, distGraph)


print("Shortest Path from", costOrg, "to", costDest, "is", costDest.estD,"Miles via",end=" ")
v = costDest
while(v):
    print(v,end=" ")
    v = v.parent
print("")

print("Least Cost from", distOrg, "to", distDest, "is", str("$" + str(distDest.estD)),"via",end=" ")
v = distDest
while(v):
    print(v,end=" ")
    v = v.parent
print("")

def randomGraph(n,p,wts=[1]):
    G = Graph()
    V = [ Vertex(x) for x in range(n) ]
    for v in V:
        G.addVertex(v)
    for v in V:
        for w in V:
            if v != w:
                if random() < p:
                    G.addDiEdge(v,w,wt=choice(wts))
    return G


# generate a bunch of random graphs and run an alg to compute shortest paths (implicitly)  
def runTrials(myFn, nVals, pFn, numTrials=25):
    nValues = []
    tValues = []
    for n in nVals:
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            G = randomGraph(n,0.2)
            start = time.time()
            myFn(G.vertices[0], G)
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues


def smallFrac(n):
    return float(5/n)



nValues = [10,50,100,150,200,300,400,500,700,1000,1200,1400,1600]
nDijkstra, tDijkstra = runTrials(dijkstra_helper, nValues,smallFrac)



plt.plot(nDijkstra, tDijkstra, "-.", color="blue", label="Dijkstra algorithm")

plt.xlabel("n")
plt.ylabel("Time(ms)")
plt.legend()
plt.title("Shortest paths on a graph with n vertices and about 5n edges")
plt.show()
