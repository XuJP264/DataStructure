from LinkedList import LinkNode
from LinkedList import LinkedList
from Queue import QueueNode
from Queue import Queue
from Stack import Stack
class TrieNode:
    def __init__(self,char):
        self.char=char
        self.isEndOfWord=False
        self.next=None
        self.child=None
class Trie:
    def __init__(self):
        self.root=TrieNode('')
    def isEmpty(self):
        return self.root is None
    def isChild(self,char,node):
        child = node.child
        while child is not None:
            if child.char==char:
                return child
            child=child.next
        return None

    def insertWord(self, word):
        node = self.root
        for char in word:
            child = self.isChild(char, node)
            if child is None:
                new_node = TrieNode(char)
                # 插入新字符到 child 链表尾部
                if node.child is None:
                    node.child = new_node
                else:
                    temp = node.child
                    while temp.next:
                        temp = temp.next
                    temp.next = new_node
                node = new_node
            else:
                node = child
        node.isEndOfWord = True  # 最后一个字符标记结尾

    def searchWord(self,word):
        node=self.root
        for char in word:
            if self.isChild(char,node) is not None:
                node=self.isChild(char,node)
            else:
                return False
        return node.isEndOfWord
    def dfs(self,node):
        if not node:
            return
        else:
            print(node.char,end=' ')
            child=node.child
            while child is not None:
                self.dfs(child)
                child=child.next
    def stackIn(self,node):
        stack=Stack()
        while node is not None:
            stack.push(node)
            node=node.next
        return stack
    def dfsNonRecursive(self,node):
        stack=Stack()
        stack.push(node)
        while not stack.is_empty():
            node=stack.pop()
            print(node.char,end=' ')
            result=self.stackIn(node.child)
            while not result.is_empty():
                stack.push(result.pop())

    def bfs(self,node):
        queue=Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            node= queue.dequeue()
            print(node.char,end=' ')
            child = node.child
            while child:
                queue.enqueue(child)
                child=child.next
    def printWord(self,node,prefix):
        if node.isEndOfWord:
            print(prefix)
        child = node.child
        while child:
            self.printWord(child,prefix+child.char)
            child = child.next


def stackIn(cur,stack):
    cur=cur.child
    s1=Stack()
    while cur:
        s1.push(cur)
        cur=cur.next
    while not s1.is_empty():
        stack.push(s1.pop())
def dfs(root):
    stack=Stack()
    stack.push(root)
    while not stack.is_empty():
        cur=stack.pop()
        print(cur.char,end=' ')
        stackIn(cur,stack)
def queueIn(cur,queue):
    cur=cur.child
    while cur:
        queue.enqueue(cur)
        cur=cur.next
def bfs(root):
    queue=Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        cur=queue.dequeue()
        print(cur.char,end=' ')
        queueIn(cur,queue)
def wordPrint(node,prefix):
    if not node:
        return
    else:
        if node.isEndOfWord==True:
            print(prefix)
        child = node.child
        while child is not None:
            wordPrint(child,prefix+child.char)
            child = child.next

if __name__ == "__main__":
    trie = Trie()

    print("✅ 插入单词: ['cat', 'cap', 'dog', 'door']")
    trie.insertWord("cat")
    trie.insertWord("cap")
    trie.insertWord("dog")
    trie.insertWord("door")
    print("\n🔍 测试查找:")
    print("search 'cat':", trie.searchWord("cat"))  # True
    print("search 'cap':", trie.searchWord("cap"))  # True
    print("search 'dog':", trie.searchWord("dog"))  # True
    print("search 'do':", trie.searchWord("do"))    # False
    print("search 'cab':", trie.searchWord("cab"))  # False

    print("\n🧭 深度优先遍历（DFS）:")
    trie.dfs(trie.root)
    print("\n🧭 非递归深度优先遍历（DFS）:")
    trie.dfsNonRecursive(trie.root)

    print("\n\n🌐 广度优先遍历（BFS）:")
    trie.bfs(trie.root)

    print("\n\n📦 打印所有单词:")
    trie.printWord(trie.root, "")
    dfs(trie.root)
    bfs(trie.root)
    wordPrint(trie.root,'')