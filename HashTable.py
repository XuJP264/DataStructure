TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY
        self.next = -1

def hash_func(key):
    return key % TABLESIZE
def Hash_func(key, i):
    return (hash_func(key) + i) % TABLESIZE
def hash_insert(key,hash_table):
    if hash_find(key,hash_table)!=-1:
        return -1
    for i in range(TABLESIZE):
        if hash_table[Hash_func(key,i)].indicator==EMPTY:
            hash_table[Hash_func(key,i)].indicator=USED
            hash_table[Hash_func(key,i)].key=key
            if i>0:
                head=hash_func(key)
                while hash_table[head].next!=-1:
                    head=hash_table[head].next
                hash_table[head].next=Hash_func(key,i)
            return Hash_func(key, i)
        else:
            continue
    return TABLESIZE+1
def hash_find(key,hash_table):
    for i in range(TABLESIZE):
        if hash_table[Hash_func(key,i)].indicator==USED and hash_table[Hash_func(key,i)].key==key:
            return Hash_func(key,i)
    return -1
if __name__ == "__main__":
    hash_table = [HashSlot() for _ in range(TABLESIZE)]

    # 1. 大量冲突测试：让所有 key 都 % 37 == 0
    print("大量冲突插入测试:")
    base = TABLESIZE  # 37
    conflict_keys = [base * i for i in range(20)]  # 0, 37, 74, ..., 都会落在同一个初始槽位
    for key in conflict_keys:
        result = hash_insert(key, hash_table)
        print(f"插入 {key}，位置: {result}")

    # 2. 测试重复插入同一个 key
    print("\n重复插入测试:")
    repeat_key = conflict_keys[0]
    result = hash_insert(repeat_key, hash_table)
    print(f"再次插入已存在的 key {repeat_key}，返回: {result}（预期为 -1）")

    # 3. 接近满表测试（补充插入）
    print("\n插入直到接近满表:")
    inserted = len(conflict_keys)
    additional_keys = [1000 + i for i in range(TABLESIZE)]  # 不太可能冲突
    for key in additional_keys:
        if inserted >= TABLESIZE - 1:
            break
        result = hash_insert(key, hash_table)
        if result != -1:
            inserted += 1
            print(f"插入 {key} 成功，位置: {result}")
        else:
            print(f"插入 {key} 失败，表可能已满")

    print(f"\n当前总插入数: {inserted}，哈希表大小: {TABLESIZE}")

    # 4. 查找测试：已插入的 & 未插入的
    print("\n查找测试（存在的 key）:")
    for key in conflict_keys[:5] + additional_keys[:5]:
        index = hash_find(key, hash_table)
        print(f"查找 {key}，找到位置: {index}")

    print("\n查找测试（不存在的 key）:")
    for key in [9999, 8888, 7777]:
        index = hash_find(key, hash_table)
        print(f"查找 {key}，结果: {index}（预期为 -1）")

    # 5. 打印表结构
    print("\n哈希表结构 (非空槽):")
    for i, slot in enumerate(hash_table):
        if slot.indicator == USED:
            print(f"索引 {i}: 键={slot.key}, next={slot.next}")

