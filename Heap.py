class Heap:
    def __init__(self,SIZE):
        self.heap=[0 for _ in range(SIZE)]
        self.heap_size=SIZE

    def __left(self,i):
        return i*2

    def __right(self,i):
        return i*2+1

    def __parent(self,i):
        return (i+1)//2

    def maxHeapify(self,i):
        l=self.__left(i)
        r=self.__right(i)
        if l<=self.heap_size and self.heap[l]>self.heap[i]:
            largest=l
        else:
            largest=i
        if r<=self.heap_size and self.heap[r]>self.heap[largest]:
            largest=r
        if largest!=i:
            self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(self.heap_size//2,-1,-1):
            self.maxHeapify(i)
    def readInHeap(self,A):
        self.heap = A
        self.heap_size = len(A)