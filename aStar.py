import math
from operator import attrgetter

# calculates the strait line distance between nodes w and d
# from latitude and longitude
def distCalc(w, d):
    wCoords = w.getCoordinates()
    dCoords = d.getCoordinates()

    latDist = wCoords[0] - dCoords[0]
    longDist = wCoords[1] - dCoords[1]

    dist = math.sqrt((latDist * latDist) + (longDist * longDist))

    return dist


def a_star_helper(w, d, G):

    # for v in G.vertices:
    #     v.estD = math.inf
    # w.estD = 0

    openList = []

    openList.append(w)
    w.setGScore(0)
    w.setFScore(distCalc(w, d))

    # for our purposes we do not allow a one hop path
    if(d in w.outNeighbors):
        w.outNeighbors.remove(d)

    while len(openList) > 0:

        current = min(openList, key=attrgetter('fScore'))

        if current == d:

            return

        else:
            openList.remove(current)
            neighbors = current.getOutNeighbors()

            for n in neighbors:
                tentativeGScore = current.getGScore() + distCalc(current, n)

                if tentativeGScore < n.getGScore():
                    n.cameFrom = current
                    n.setGScore(tentativeGScore)
                    n.setFScore(n.getGScore() + distCalc(n, d))
                    if n not in openList:
                        openList.append(n)
            
    # if the while loop ends
    # path could not be found 



def a_star(w, d, G):

    a_star_helper(w, d, G)

    # starting from destination retrace the path
    path = []
    current = d
    path.append(current)
    while current.cameFrom:
        path.append(current.cameFrom)
        current = current.cameFrom
    path.reverse()

    return path

