import heapq
import random

class MedianHeap:
    """
    Max heap for lower half. Min heap for upper half.
    Median = maxHeap[0] <-> minHeap[0]
    """
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    """
    Min Heap Implementation
    """
    # Get top of min heap
    def peekMinHeap(self):
        return self.minHeap[0] if self.minHeap else float('+inf')

    # Append to end of min heap (trickle up included)
    def pushMinHeap(self, data):
        heapq.heappush(self.minHeap, data)

    # Push to top of min heap (trickle down included)
    def putTopMinHeap(self, data):
        return heapq.heapreplace(self.minHeap, data)

    # Get size of min heap
    def sizeMinHeap(self):
        return len(self.minHeap)

    """
    Max Heap Implementation
    (A negative min heap is a max heap)
    """
    # Get top of max heap
    def peekMaxHeap(self):
        return -self.maxHeap[0] if self.maxHeap else float('-inf')

    # Append to end of max heap (trickle up included)
    def pushMaxHeap(self, data):
        heapq.heappush(self.maxHeap, data * -1)

    # Push to top of max heap (trickle down included)
    def putTopMaxHeap(self, data):
        return heapq.heapreplace(self.maxHeap, data * -1)

    # Get size of max heap
    def sizeMaxHeap(self):
        return len(self.maxHeap)

    def __str__(self):
        print("Lower: ", self.peekMaxHeap(), " | Upper: ", self.peekMinHeap(), " | Even: ", len(self) % 2 == 0, " | Median: ", self.getMedian(), )
        revList = self.maxHeap[::-1]
        return "".join([" ".join(map(str, map(lambda d: -d, revList))),
                        " | ",
                        " ".join(map(str, self.minHeap)),
                        "\n"])

    """
    Median Heap Methods
    """

    def add(self, data):
        print("Adding: ", data)
        # Even
        if (self.sizeMinHeap() == self.sizeMaxHeap()):
            # Data is below upper bound, add to max heap
            if data < self.peekMinHeap():
                self.pushMaxHeap(data)
            else:
                self.pushMaxHeap(self.putTopMinHeap(data) )
        # Odd
        else:
            # Data is above lower bound, add to min heap
            if data > self.peekMaxHeap():
                self.pushMinHeap(data)
            else:
                # Taking num out of max heap need to negate negative
                self.pushMinHeap(self.putTopMaxHeap(data) * -1)
        print(self.__str__())

    def getMedian(self):
        # Even
        if (self.sizeMinHeap() == self.sizeMaxHeap()):
            return (self.peekMaxHeap() + self.peekMinHeap()) / 2.0
        # Odd
        else:
            return self.peekMaxHeap()

    def __len__(self):
        return len(self.maxHeap) + len(self.minHeap)


medHeap = MedianHeap()
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))
medHeap.add(random.randint(1,100))

