from graph import *
from vertex import *
from aStarVertex import *
from dijkstra import *
from aStar import *
from aStarVertex import *
from random import *

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
astarGraph = Graph()

# read data from dataset for dijkstra
dijkstra_df = pd.read_csv('./dataSets/cleaned.csv')
airportlonglat = pd.read_csv('./dataSets/airportswithcodes.csv')
airportlonglat = airportlonglat.set_index("code")
#


# Tracks index of vertice in graph
VertIndex = []

for idx, row in dijkstra_df.iterrows():
    if row[0] not in VertIndex:
        costGraph.addVertex(Vertex(row[0]))
        distGraph.addVertex(Vertex(row[0]))

        astarGraph.addVertex(AStarVertex(row[0],airportlonglat.loc[row[0],"lat"],airportlonglat.loc[row[0],"long"]))

        VertIndex.append(row[0])

    if row[1] not in VertIndex:
        costGraph.addVertex(Vertex(row[1]))
        distGraph.addVertex(Vertex(row[1]))
        
        astarGraph.addVertex(AStarVertex(row[1],airportlonglat.loc[row[1],"lat"],airportlonglat.loc[row[1],"long"]))

        VertIndex.append(row[1])

    costGraph.addDiEdge(costGraph.vertices[VertIndex.index(
        row[0])], costGraph.vertices[VertIndex.index(row[1])], row[2])
    distGraph.addDiEdge(distGraph.vertices[VertIndex.index(
        row[0])], distGraph.vertices[VertIndex.index(row[1])], row[3])
        
    astarGraph.addDiEdge(astarGraph.vertices[VertIndex.index(
        row[0])], astarGraph.vertices[VertIndex.index(row[1])], row[3])

costOrg = costGraph.vertices[VertIndex.index('SFB')]
distOrg = distGraph.vertices[VertIndex.index('SFB')]
costDest = costGraph.vertices[VertIndex.index('YNG')]
distDest = distGraph.vertices[VertIndex.index('YNG')]

aStarOrg = astarGraph.vertices[VertIndex.index('ABE')]
aStarDest = astarGraph.vertices[VertIndex.index('YNG')]

dijkstra(costOrg, costGraph)
dijkstra(distOrg, distGraph)

aStarPath = a_star(aStarOrg, aStarDest, astarGraph)
for node in aStarPath:
    print(node)


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


def randomDijkstra(n, p, wts=[1]):
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

def randomAStarGraph(n, p, wts=[1]):
    graph = Graph()

    minLat = -20.0
    maxLat = 50.0
    minLong = -150.0
    maxLong = -60.0
    V = []
    for x in range(n):
        # generate random latitude and longitude
        latitude = uniform(minLat, maxLat)
        longitude = uniform(minLong, maxLong)
        V.append(AStarVertex(1,latitude, longitude))
        
    for v in V:
        graph.addVertex(v)
    for v in V:
        for w in V:
            if v != w:
                if random() < p:
                    graph.addDiEdge(v, w, wt=choice(wts))
    return graph

# generate a bunch of random graphs and run an alg to compute shortest paths (implicitly)
def runDijkstraTrials(dijkstra_function, xVals, numTrials=50):
    x_values = []
    y_values = []
    for n in xVals:
        # here we are running dijkstra's algorithm multiple times and calculate average to get a better estimate
        runtime = 0
        for t in range(numTrials):
            newGraph = randomDijkstra(n, 0.2)
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


def runAStarTrials(dijkstra_function, xVals, numTrials=50):
    x_values = []
    y_values = []
    for n in xVals:
        # here we are running dijkstra's algorithm multiple times and calculate average to get a better estimate
        runtime = 0
        for t in range(numTrials):
            newGraph = randomAStarGraph(n, 0.2)
            # start timer
            start = time.time()
            dijkstra_function(newGraph.vertices[0], newGraph.vertices[len(newGraph.vertices) - 1], newGraph)
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
x_axis, y_axis = runDijkstraTrials(dijkstra_helper, xvalues)
x_axis2, y_axis2 = runAStarTrials(a_star_helper, xvalues)

# plotting the graph
graph.plot(x_axis, y_axis, "-.", color="blue", label="Dijkstra algorithm")
graph.plot(x_axis2, y_axis2, "-", color="red", label="A Star Algorithm")

# title and legend
graph.title("Running times of Dijkstra's vs A* Algorithm")
graph.legend()


# x and y labels for the graph
graph.xlabel("n")
graph.ylabel("Time(ms)")


graph.show()




