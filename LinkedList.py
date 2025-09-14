class LinkNode:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def isEmpty(self):
        return self.head is None
    def appendNode(self,data):
        newNode = LinkNode(data)
        p = self.head
        if self.isEmpty():
            self.head = LinkNode(data)
        else:
            while p.next is not None:
                p=p.next
            p.next = newNode
        self.size+=1
    def insertNode(self,data,index):
        if not (0<=index and index<=self.size):
            print("the index is invalid")
            return
        else:
            newNode = LinkNode(data)
            pre=None
            p=self.head
            if index==0:
                newNode.next=p
                self.head=newNode
            else:
                for _ in range(index):
                    pre=p
                    p=p.next
                pre.next=newNode
                newNode.next=p
            self.size+=1
    def deleteNodeByIndex(self,index):
        if not (0<=index<self.size):
            print("the index is invalid")
            return
        else:
            p=self.head
            pre=None
            self.size-=1
            if index==0:
                self.head= p.next
                return
            for _ in range(index):
                pre=p
                p=p.next
            pre.next=p.next
    def search(self,target):
        p=self.head
        index=0
        while p:
            if p.data==target:
                return index
            p=p.next
            index+=1
        return None
    def deleteNodeByValue(self,target):
        index = self.search(target)
        if index is not None:
            self.deleteNodeByIndex(index)
        else:
            print('target not found')
    def display(self):
        print("the Linked List length is: ",self.size)
        p=self.head
        while p:
            print(p.data,end=' ')
            p=p.next
class TestLinkedList:
    @staticmethod
    def run_tests():
        ll = LinkedList()

        print("测试 appendNode...")
        ll.appendNode(10)
        ll.appendNode(20)
        ll.appendNode(30)
        ll.display()

        print("\n测试 insertNode...")
        ll.insertNode(5, 0)      # 插入头部
        ll.insertNode(25, 3)     # 插入中间
        ll.insertNode(35, ll.size)  # 插入末尾
        ll.display()

        print("\n测试 deleteNodeByIndex...")
        ll.deleteNodeByIndex(0)  # 删除头
        ll.deleteNodeByIndex(2)  # 删除中间
        ll.deleteNodeByIndex(ll.size - 1)  # 删除尾
        ll.display()

        print("\n测试 search...")
        print("search 20:", ll.search(20))
        print("search 99:", ll.search(99))

        print("\n测试 deleteNodeByValue...")
        ll.deleteNodeByValue(20)
        ll.deleteNodeByValue(99)  # 不存在
if __name__ == "__main__":
    TestLinkedList.run_tests()
