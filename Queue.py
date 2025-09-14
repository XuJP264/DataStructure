class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  # 队头
        self.tail = None  # 队尾
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue.")
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:  # 队列变空
            self.tail = None
        self.size -= 1
        return removed_data

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data

    def __len__(self):
        return self.size
if __name__ == "__main__":
    q = Queue()
    print("Is empty?", q.isEmpty())

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue size:", len(q))
    print("Peek:", q.peek())

    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Dequeue from empty:", q.dequeue())
