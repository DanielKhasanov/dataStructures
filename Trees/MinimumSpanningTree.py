from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.neighbors = {}
        self.val = val
        self.family = "Forest " + val

    def addConnection(self, weight, node):
        self.neighbors[node.val] = weight
        self.isLeafNode = False

    def printConnections(self):
        print("Node " + self.val + " is connected to ", [n for n in self.neighbors])

alpha = "ABCDEFGHIJKLMN"
edges = [(11, "A", "B"),
         (21, "B", "C"),
          (6, "C", "D"),
          (4, "D", "E"),
         (5, "B", "G"),
         (7, "D", "I"),
         (8, "E", "J"),
         (14, "F", "G"),
         (16, "G", "H"),
         (12, "H", "I"),
         (19, "I", "J"),
         (8, "G", "K"),
         (13, "H", "L"),
         (22, "I", "M"),
         (5, "J", "N"),
         (11, "K", "L"),
         (20, "L", "M"),
         (10, "M", "N")
         ]

class Graph:
    def __init__(self):
        self.numVertex = 0
        self.nodeDict = {}
        self.edges = PriorityQueue()
        self.forestDict = {}
        self.cyclicEdges = []

    def updateForest(self, oldForest, newForest):
        # Combine the two forestes
        self.forestDict[newForest] += self.forestDict[oldForest]

        # Update the forest values
        for node in self.forestDict[newForest]:
            node.family = newForest

        # Delete the older forest
        del self.forestDict[oldForest]

    def addVertex(self, val):
        newNode = Node(val)
        self.nodeDict[newNode.val] = newNode
        self.numVertex += 1
        self.forestDict[newNode.family] = [newNode]

    def addEdge(self, newEdge):
        # Add tuples to priority queue
        self.edges.put(newEdge)

    def MST_addEdge(self, newEdge):
        # Retrieve nodes from dictionary
        startNode = self.nodeDict[newEdge[1]]
        endNode = self.nodeDict[newEdge[2]]
        weight = newEdge[0]

        # Link the two nodes
        startNode.addConnection(weight, endNode)
        endNode.addConnection(weight, startNode)
        #print("Connected ", startNode.val, " and ", endNode.val)

        # The two nodes now share a family
        self.updateForest(startNode.family, endNode.family)

    def computeMST(self):
        while not self.edges.empty():
            # Grab next min edge
            # Retrieve nodes from dictionary
            nextMinEdge = self.edges.get()
            startNode = self.nodeDict[nextMinEdge[1]]
            endNode = self.nodeDict[nextMinEdge[2]]

            # Check for same forest/family
            if startNode.family != endNode.family:
                self.MST_addEdge(nextMinEdge)
            else:
                #print("Nodes: ", nextMinEdge[1], nextMinEdge[2], " share the same family")
                self.cyclicEdges.append(nextMinEdge)

    def showConnections(self):
        for nKey in self.nodeDict:
            self.nodeDict[nKey].printConnections()
        print("Filtered Edges")
        print(self.cyclicEdges)


# Regular Dry Run
G = Graph()
for v in alpha:
    G.addVertex(v)
for e in edges:
    G.addEdge(e)
G.computeMST()
G.showConnections()

# With newly added edges
alpha2 = "ABCDEFGHIJKLMNO"
edges2 = [(11, "A", "B"),
         (21, "B", "C"),
          (6, "C", "D"),
          (4, "D", "E"),
         (5, "B", "G"),
         (7, "D", "I"),
         (8, "E", "J"),
         (14, "F", "G"),
         (16, "G", "H"),
         (12, "H", "I"),
         (19, "I", "J"),
         (8, "G", "K"),
         (13, "H", "L"),
         (22, "I", "M"),
         (5, "J", "N"),
         (11, "K", "L"),
         (20, "L", "M"),
         (10, "M", "N"),
         (6, "K", "O"),
         (7, "L", "O"),
         (1, "M", "O"),
         (3, "N", "O"),
         (20, "A", "O"),
         (9, "B", "O"),
         (13, "C", "O"),
         (15, "D", "O")
         ]

nG = Graph()
for v in alpha2:
    nG.addVertex(v)
for e in edges2:
    nG.addEdge(e)
nG.computeMST()
nG.showConnections()

# fG = Graph()
# for v in alpha2:
#     fG.addVertex(v)
# for e in edges2:
#     fG.addEdge(e)
# fG.computeMST()
# fG.showConnections()




