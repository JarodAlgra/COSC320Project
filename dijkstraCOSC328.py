from graphStuff import *
from random import random
from random import choice
import heapdict as heapdict # you will need to install heapdict to use this
import time

#you need to install matplotlib to be able to plot
import matplotlib
import numpy as np #you need to install numpy package
import matplotlib.pyplot as plt

#test a graph
# make a random graph
# This is G(n,p), where we have n vertices and each (directed) edge is present with probability p.
# if you pass in a set of weights, then the weights are chosen uniformly from that set.
# otherwise all weights are 1
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

# Dijkstra's algorithm for shortest paths
# BFS only works on unweighted graphs.  Dijkstra's algorithm will work on weighted graphs.
# first let's implement this with an array.
def dijkstraDumb(w,G):
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

def dijkstraDumb_shortestPaths(w,G):
    dijkstraDumb(w,G)
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

# test on a random grap

# now let's try this with a heap
def dijkstra(w,G):
    for v in G.vertices:
        v.estD = math.inf
    w.estD = 0
    unsureVertices = heapdict.heapdict()
    for v in G.vertices:
        unsureVertices[v] = v.estD
    while len(unsureVertices) > 0:
        # find the u with the minimum estD, using the heap
        u, dist = unsureVertices.popitem() 
        if u.estD == math.inf:
            # then there is nothing more that I can reach
            return
        # update u's neighbors
        for v,wt in u.getOutNeighborsWithWeights():
            if u.estD + wt < v.estD:
                v.estD = u.estD + wt
                unsureVertices[v] = u.estD + wt #update the key in the heapdict
                v.parent = u
    # that's it!  Now each vertex holds estD which is its distance from w

def dijkstra_shortestPaths(w,G):
    dijkstra(w,G)
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
        print('From', w, 'to', v, [str(x) for x in path])

# test on a random graph


# generate a bunch of random graphs and run an alg to compute shortest paths (implicitly)  
def runTrials(myFn, nVals, pFn, numTrials=25):
    nValues = []
    tValues = []
    for n in nVals:
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            G = randomGraph(n, pFn(n))  #Random graph on n vertices with about pn^2 edges
            start = time.time()
            myFn( G.vertices[0], G ) 
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

def smallFrac(n):
    return float(5/n)


G = Graph()
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
for v in [A, B, C, D, E]:
    G.addVertex(v)
G.addBiEdge(A, B, 2)
G.addBiEdge(A, C, 4)
G.addBiEdge(A, D, 1)
G.addBiEdge(B, D, 6)
G.addBiEdge(B, E, 9)
G.addBiEdge(C, D, 4)
G.addBiEdge(D, E, 2)

print(G)

print("Shortest path from A to all other nodes")
dijkstra(G.vertices[0], G)
dijkstra_shortestPaths(G.vertices[0], G)

G1 = Graph()
u = Vertex('u')
v = Vertex('v')
x = Vertex('x')
y = Vertex('y')
z = Vertex('z')
for vertex in [u, v, x, y, z]:
    G1.addVertex(vertex)
G1.addBiEdge(u, v, 1)
G1.addBiEdge(u, y, 2)
G1.addBiEdge(v, x, 3)
G1.addBiEdge(v, z, 6)
G1.addBiEdge(x, y, 3)
G1.addBiEdge(x, z, 1)
print("\n\n")
print(G1)
print("Shortest path from z to all other nodes")
dijkstra(G1.vertices[4], G1)
dijkstra_shortestPaths(G1.vertices[4], G1)
