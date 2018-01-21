class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return " ".join(map(str,self.items))

newQ = Queue()
testList = [4,5,6,7,8]
for num in testList:
    newQ.enqueue(num)

print(newQ)
