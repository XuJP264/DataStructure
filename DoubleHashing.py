TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1
DELETED = 2


class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY


def hash1(key):
    return key % TABLESIZE

def hash2(key):
    return (key % PRIME) + 1

def hash_func(key, i):
    return (hash1(key) + i * hash2(key)) % TABLESIZE
def hash_find(key, hash_table):
    for i in range(TABLESIZE):
        idx = hash_func(key, i)
        if hash_table[idx].indicator == EMPTY:
            return False
        if hash_table[idx].indicator == USED and hash_table[idx].key == key:
            return True
    return False


def hash_insert(key, hash_table):
    first_deleted_index = -1
    for i in range(TABLESIZE):
        idx = hash_func(key, i)
        slot = hash_table[idx]

        # Track DELETED slot
        if slot.indicator == DELETED and first_deleted_index == -1:
            first_deleted_index = idx

        # Key already exists
        if slot.indicator == USED and slot.key == key:
            return -1

        # If EMPTY, we can insert if no key found
        if slot.indicator == EMPTY:
            if first_deleted_index != -1:
                hash_table[first_deleted_index].indicator = USED
                hash_table[first_deleted_index].key = key
                return i + 1  # i starts from 0, so +1 comparisons done
            else:
                slot.indicator = USED
                slot.key = key
                return i + 1
    # Table full if loop ends
    return TABLESIZE


def hash_delete(key, hash_table):
    for i in range(TABLESIZE):
        idx = hash_func(key, i)
        slot = hash_table[idx]

        if slot.indicator == EMPTY:
            return -1
        if slot.indicator == USED and slot.key == key:
            slot.indicator = DELETED
            return i + 1
    return -1

def run_test():
    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    print("🧪 测试开始...\n")

    keys_to_insert = [10, 47, 84, 121, 13, 50, 87, 124]  # 有冲突
    for key in keys_to_insert:
        result = hash_insert(key, hash_table)
        if result >= 0:
            print(f"插入 {key} 成功，比较次数: {result}")
        else:
            print(f"插入 {key} 失败（重复）")

    # 再插入一个重复的 key
    print("\n插入重复 key 10:")
    print("返回：", hash_insert(10, hash_table))  # 应该是 -1

    # 删除部分 key
    print("\n删除 key 47, 121:")
    print(f"删除 47，比较次数: {hash_delete(47, hash_table)}")
    print(f"删除 121，比较次数: {hash_delete(121, hash_table)}")

    # 删除一个不存在的 key
    print(f"删除不存在 key 9999，返回: {hash_delete(9999, hash_table)}")

    # 打印当前哈希表状态
    print("\n当前哈希表内容（* 表示已删除）:")
    for i in range(TABLESIZE):
        marker = '*' if hash_table[i].indicator == DELETED else ' '
        print(f"{i:2}: {hash_table[i].key} {marker}")


if __name__ == "__main__":
    run_test()
