from graph import *
from vertex import *
from dijkstra import *
from random import random
from random import choice
import time
import csv
import pandas as pd

# you need to install matplotlib to be able to plot
import matplotlib
import numpy as np  # you need to install numpy package
import matplotlib.pyplot as graph

# graphs
costGraph = Graph()
distGraph = Graph()

# read data from dataset
df = pd.read_csv('./dataSets/cleaned.csv')

# Tracks index of vertice in graph
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

    costGraph.addDiEdge(costGraph.vertices[VertIndex.index(
        row[0])], costGraph.vertices[VertIndex.index(row[1])], row[2])
    distGraph.addDiEdge(distGraph.vertices[VertIndex.index(
        row[0])], distGraph.vertices[VertIndex.index(row[1])], row[3])

costOrg = costGraph.vertices[VertIndex.index('SFB')]
distOrg = distGraph.vertices[VertIndex.index('SFB')]
costDest = costGraph.vertices[VertIndex.index('YNG')]
distDest = distGraph.vertices[VertIndex.index('YNG')]

dijkstra(costOrg, costGraph)
dijkstra(distOrg, distGraph)


print("Shortest Path from", costOrg, "to", costDest,
      "is", costDest.estD, "Miles via", end=" ")
v = costDest
while(v):
    print(v, end=" ")
    v = v.parent
print("")

print("Least Cost from", distOrg, "to", distDest, "is",
      str("$" + str(distDest.estD)), "via", end=" ")
v = distDest
while(v):
    print(v, end=" ")
    v = v.parent
print("")


def randomGraph(n, p, wts=[1]):
    graph = Graph()
    V = [Vertex(x) for x in range(n)]
    for v in V:
        graph.addVertex(v)
    for v in V:
        for w in V:
            if v != w:
                if random() < p:
                    graph.addDiEdge(v, w, wt=choice(wts))
    return graph


# generate a bunch of random graphs and run an alg to compute shortest paths (implicitly)
def runTrials(dijkstra_function, xVals, numTrials=50):
    x_values = []
    y_values = []
    for n in xVals:
        # here we are running dijkstra's algorithm multiple times and calculate average to get a better estimate
        runtime = 0
        for t in range(numTrials):
            newGraph = randomGraph(n, 0.2)
            # start timer
            start = time.time()
            dijkstra_function(newGraph.vertices[0], newGraph)
            # end timer
            end = time.time()
            # calculate total runtime
            runtime += (end - start) * 1000
        # calculate average runtime
        runtime = runtime/numTrials
        # add them to the appropriate arrays
        x_values.append(n)
        y_values.append(runtime)
    return x_values, y_values


xvalues = [10, 50, 100, 150, 200, 300, 400, 500, 700, 1000, 1200, 1400, 1600]
x_axis, y_axis = runTrials(dijkstra_helper, xvalues)

# plotting the graph
graph.plot(x_axis, y_axis, "-.", color="blue", label="Dijkstra algorithm")

# title and legend
graph.title("Running time of Dijkstra's Algorithm")
graph.legend()


# x and y labels for the graph
graph.xlabel("n")
graph.ylabel("Time(ms)")


graph.show()
