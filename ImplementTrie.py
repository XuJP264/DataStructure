class TrieNode:
    def __init__(self,char):
        self.char=char
        self.next=None
        self.child=None
        self.isEndOfWord=False
def isChild(node,char):
    node=node.child
    while node:
        if node.char==char:
            return node
        else:
            node=node.next
class Trie:
    def __init__(self):
        self.root=TrieNode('')
    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            if isChild(node,char) is not None:
                node=isChild(node,char)
            else:
                if node.child:
                    while node.next:
                        node=node.next
                    node.next=TrieNode(char)
                else:
                    node.child=TrieNode(char)
        node.isEndOfWord=True

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if isChild(node,char):
                node=isChild(node,char)
            else:
                return False
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if isChild(node, char):
                node = isChild(node, char)
            else:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)