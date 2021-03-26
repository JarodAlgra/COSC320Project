import math

class Vertex:
    def __init__(self, v):
        self.inNeighbors = [] # list of pairs (nbr, wt), where nbr is a CS161Vertex and wt is a weight
        self.outNeighbors = [] # same as above
        self.value = v
        # useful for DFS/BFS/Dijkstra/Bellman-Ford
        self.inTime = None
        self.outTime = None
        self.status = "unvisited"
        self.parent = None
        self.estD = math.inf

    def hasOutNeighbor(self,v):
        if v in self.getOutNeighbors():
            return True
        return False

    def hasInNeighbor(self,v):
        if v in self.getInNeighbors():
            return True
        return False

    def hasNeighbor(self,v):
        if v in self.getInNeighbors() or v in self.getOutNeighbors():
            return True
        return False

    def getOutNeighbors(self):
        return [ v[0] for v in self.outNeighbors ]

    def getInNeighbors(self):
        return [ v[0] for v in self.inNeighbors ]

    def getOutNeighborsWithWeights(self):
        return self.outNeighbors

    def getInNeighborsWithWeights(self):
        return self.inNeighbors

    def addOutNeighbor(self,v,wt):
        self.outNeighbors.append((v,wt))

    def addInNeighbor(self,v,wt):
        self.inNeighbors.append((v,wt))

    def __str__(self):
        return str(self.value)
