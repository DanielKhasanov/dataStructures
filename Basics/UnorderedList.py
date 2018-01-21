
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, new):
        self.next = new



class UnorderedList():

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def contains(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if(current.getData() == item):
                found = True
            else:
                current = current.getNext()

        return found

    def isEmpty(self):
        return self.head == None

    def remove(self, item):
        found = False
        previous = None
        current = self.head

        while not found:
            if current.getData() == item:
                found = True
            else:
                #move along
                previous = current
                current = current.getNext()
        #head is a match
        if previous == None:
            self.head = current.getNext()
        #delete the code
        else:
            previous.next = current.getNext()




mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.contains(93))
print(mylist.contains(100))

mylist.add(100)
print(mylist.contains(100))


