
import math

# Implementation of directed graphs with weighted edges

# This is a directed graph class.
# It can also be used as an undirected graph by adding edges in both directions.
class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self,n):
        self.vertices.append(n)

    # add a directed edge from Node u to Node v
    def addDiEdge(self,u,v,wt=1):
        u.addOutNeighbor(v,wt=wt)
        v.addInNeighbor(u,wt=wt)

    # add edges in both directions between u and v
    def addBiEdge(self,u,v,wt=1):
        self.addDiEdge(u,v,wt=wt)
        self.addDiEdge(v,u,wt=wt)

    # get a list of all the directed edges
    # directed edges are a list of two vertices and a weight
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            for u, wt in v.getOutNeighborsWithWeights():
                ret.append( [v,u,wt] )
        return ret

    def __str__(self):
        ret = "Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b,wt in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + "; wt:" + str(wt) + ") "
        ret += "\n"
        return ret




