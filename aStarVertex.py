import math

class AStarVertex:
    def __init__(self, v, latitude, longitude):
        self.inNeighbors = [] # list of pairs (nbr, wt), where nbr is a CS161Vertex and wt is a weight
        self.outNeighbors = [] # same as above
        self.value = v
        self.latitude = latitude
        self.longitude = longitude
        self.status = "unvisited"
        self.cameFrom = None
        self.gScore = math.inf
        self.fScore = math.inf

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

    def getCoordinates(self):
        return (self.latitude, self.longitude)
    
    def getGScore(self):
        return self.gScore
    
    def getFScore(self):
        return self.fScore

    def setGScore(self, value):
        self.gScore = value
        
    def setFScore(self, value):
        self.fScore = value
    
    def addOutNeighbor(self,v,wt):
        self.outNeighbors.append((v,wt))

    def addInNeighbor(self,v,wt):
        self.inNeighbors.append((v,wt))

    def __str__(self):
        return str(self.value)
