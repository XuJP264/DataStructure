USED = 1
EMPTY = 0

class HashSlot:
    def __init__(self):
        self.key = -1
        self.indicate = EMPTY
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [HashSlot() for _ in range(size)]

    def hashFunc(self, key):
        return key % self.size

    def search(self, data):
        node = self.table[self.hashFunc(data)]
        while node:
            if node.indicate == USED and node.key == data:
                return node
            else:
                node = node.next
        return None

    def insert(self, data):
        node = self.table[self.hashFunc(data)]
        if node.indicate == USED:
            while node.next:
                node = node.next
            node.next = HashSlot()
            node.next.key = data
            node.next.indicate = USED
        else:
            node.indicate = USED
            node.key = data

# ========== 测试 ==========

ht = HashTable(5)
data_list = [7, 12, 17, 22]

for data in data_list:
    ht.insert(data)

# 搜索测试
for data in data_list + [99]:
    result = ht.search(data)
    if result:
        print(f"Found {data} at slot with key {result.key}")
    else:
        print(f"{data} not found")
