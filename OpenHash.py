# 状态常量
EMPTY = 0
USED = 1
DELETED = 2

class HashSlot:
    def __init__(self):
        self.key = None
        self.status = EMPTY

    def __repr__(self):
        if self.status == USED:
            return f"{self.key}"
        elif self.status == DELETED:
            return "DELETED"
        else:
            return "EMPTY"

class HashTableOpen:
    def __init__(self, size):
        self.size = size
        self.table = [HashSlot() for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def _hashFunction(self, key, i):
        return (self._hash(key) + i) % self.size

    def insert(self, data):
        temp = None
        for i in range(self.size):
            index = self._hashFunction(data, i)
            slot = self.table[index]

            if slot.status == EMPTY:
                if temp is not None:
                    self.table[temp].status = USED
                    self.table[temp].key = data
                    return temp
                slot.status = USED
                slot.key = data
                return index

            elif slot.status == DELETED and temp is None:
                temp = index

            elif slot.status == USED and slot.key == data:
                return -1  # duplicate
        return self.size  # table full

    def delete(self, data):
        for i in range(self.size):
            index = self._hashFunction(data, i)
            slot = self.table[index]

            if slot.status == EMPTY:
                return -1  # Not found

            elif slot.status == USED and slot.key == data:
                slot.status = DELETED
                slot.key = None
                return index
        return self.size  # Not found

    def search(self, key):
        for i in range(self.size):
            index = self._hashFunction(key, i)
            slot = self.table[index]

            if slot.status == EMPTY:
                return -1
            elif slot.status == USED and slot.key == key:
                return index
            # continue for DELETED or mismatched USED
        return -1

    def __str__(self):
        return "[" + ", ".join(str(slot) for slot in self.table) + "]"
def test_hash_table():
    ht = HashTableOpen(5)
    print("Initial:", ht)

    # 插入两个冲突的 key
    assert ht.insert(1) != -1
    assert ht.insert(6) != -1  # 与1冲突
    print("After inserts:", ht)

    # 搜索
    assert ht.search(1) != -1
    assert ht.search(6) != -1
    assert ht.search(11) == -1  # 不存在

    # 删除一个元素
    assert ht.delete(1) != -1
    print("After delete 1:", ht)
    assert ht.search(1) == -1

    # 插入一个新元素，应该复用被删除的位置
    assert ht.insert(11) != -1
    print("After insert 11:", ht)
    assert ht.search(11) != -1

    print("✅ All tests passed!")

# 运行测试
if __name__ == "__main__":
    test_hash_table()
