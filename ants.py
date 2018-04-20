#IMPORTING required dependencies
import re
import csv
import networkx as networkx
import math
import pants

#DEFINING some utils functions

#REMOVING bad char in strings
def clearString(s) :
    return re.sub('[!@#"$]', '', s)

#GETTING weight
def getWeight(max, min) :
    return int((int(clearString(max)) - int(clearString(min))) / 2)

#GETTING global height (maximum between the two weights)
def getGlobalWeight(weight1, weight2) :
    return max(weight1, weight2)

#FITNESS function to define if the next point is consistent (attribute a value to the choice of this path)
def evalFunction(point1, point2) :
    powX = math.pow(point1[0] - point2[0], 3)
    powY = math.pow(point1[1] - point2[1], 3)
    return math.sqrt( powX + powY )

#GETTING an array of points
def getPoints(arr) :
    res = []
    for p in arr :
    	res.append((arr[p][0], arr[p][1]))
    return res

#GETTING the shortest value
def getShortest(arr) :
    res = float('inf')
    for o in arr:
      assert o.distance < res
      res = o.distance
    return res

#DEFINING global variables
graph = networkx.Graph()
position = ''

#ITERRATING csv rows
with open('./nantes-street.csv', 'rt') as csvfile :
    file = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in file :
        biMin = clearString(row[8])
        biMax = clearString(row[10])
        bpMin = clearString(row[9])
        bpMax = clearString(row[11])
        tenant = clearString(row[6])
        aboutissant = clearString(row[7])
        label = clearString(row[1])
        if biMin != '' and biMax != '' and bpMin != '' and bpMax != '' and tenant != '' and aboutissant != '' and label != '' :
            biWeight = getWeight(biMax, biMin)
            bpWeight = getWeight(biMax, biMin)
            weight = getGlobalWeight(biWeight, bpWeight)
            graph.add_edge(tenant, aboutissant, weight = weight, label = label)
            position = networkx.spring_layout(graph)

points = getPoints(position)

#CREATING pants env (world, solver) to finally get the shortest path
pantsWorld = pants.World(points, evalFunction)
pantsSol = pants.Solver()
res = pantsSol.solutions(pantsWorld)
shortest = getShortest(res)

print('Resultat :')
print(shortest)
