from graph import *
from vertex import *
from dijkstra import *
from aStarVertex import *
from random import random
from random import choice
import time
import csv
import pandas as pd


testV = AStarVertex(10, 11, 12)
coords = testV.getCoordinates()
print("Latitude: ",  coords[0])
print("Longitude: ", coords[1])