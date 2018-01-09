class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return " ".join(map(str,self.items))

newDQ = Deque()
testList = [4,5,6,7,8]

for num in testList:
    newDQ.addFront(num)
    newDQ.addRear(num)

print(newDQ)