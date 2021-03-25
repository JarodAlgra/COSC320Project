from graphStuff import *
from random import random
from random import choice
import heapdict as heapdict # you will need to install heapdict to use this
import time
import csv
import pandas as pd

#you need to install matplotlib to be able to plot
import matplotlib
import numpy as np #you need to install numpy package
import matplotlib.pyplot as plt

#declare graph
G = Graph()

# read data from dataset
# add vertices to graph


df = pd.read_csv('./dataSets/cleaned.csv')

orglist = []
allorgs = df.groupby(by="Origin")
wts = [1]

#Tracks index of vertice in graph
VertIndex = []

for idx, row in df.iterrows():
    if row[0] not in VertIndex:
        G.addVertex(Vertex(row[0]))
        VertIndex.append(row[0])

    if row[1] not in VertIndex:
        G.addVertex(Vertex(row[1]))
        VertIndex.append(row[1])

    G.addDiEdge(G.vertices[VertIndex.index(row[0])],G.vertices[VertIndex.index(row[1])],row[2])


# for vert in allorgs.groups:
#     orglist.append(Vertex(vert))

# for v in orglist:
#     G.addVertex(v)
# for v in orglist:
#     for w in orglist:
#         if v != w:
#             if random() < 0.2:
#                 G.addDiEdge(v, w, wt=choice(wts))



def dijkstra_helper(w,G):
    for v in G.vertices:
        v.estD = math.inf
    w.estD = 0
    unsureVertices = G.vertices[:]
    while len(unsureVertices) > 0:
        # find the u with the minimum estD in the dumbest way possible
        u = None
        minD = math.inf
        for x in unsureVertices:
            if x.estD < minD:
                minD = x.estD
                u = x
        if u == None:
            # then there is nothing more that I can reach
            return
        # update u's neighbors
        for v,wt in u.getOutNeighborsWithWeights():
            if u.estD + wt < v.estD:
                v.estD = u.estD + wt
                v.parent = u
        unsureVertices.remove(u)
    # that's it!  Now each vertex holds estD which is its distance from w

def dijkstra(w,G):
    dijkstra_helper(w,G)
    # okay, now what are all the shortest paths?
    for v in G.vertices:
        if v.estD == math.inf:
            print("Cannot reach " + str(v))
            continue
        path = []
        current = v
        while current != w:
            path.append(current)
            current = current.parent
        path.append(current)
        path.reverse()
        print([ str(x) for x in path ])


org  = G.vertices[VertIndex.index('SFB')]
dest = G.vertices[VertIndex.index('YNG')]

dijkstra(org, G)


print("distance from", org, "to", dest, "is", dest.estD)