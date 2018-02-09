# Adjacency List Implementation

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertext(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, item):
        if item in self.vertList:
            return self.vertList[item]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, start, end, cost = 0):
        if start not in self.vertList:
            _ = self.addVertext(start)
        if end not in self.vertList:
            _ = self.addVertext(end)
        self.vertList[start].addNeighbor(self.vertList[end], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
