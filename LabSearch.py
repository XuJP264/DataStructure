import random
def testSet(n):
    return [random.randint(0,n*3) for _ in range(n)]
def merge(leftArr,rightArr):
    result=[]
    i=0
    j=0
    while leftArr[i:] and rightArr[j:]:
        if leftArr[i][0]<rightArr[j][0]:
            result.append(leftArr[i])
            i+=1
        else:
            result.append(rightArr[j])
            j+=1
    result.extend(leftArr[i:])
    result.extend(rightArr[j:])
    return result
def dual_sorted_search(A, size, K, dual_index):
    Arr=[(A[i],i) for i in range(size)]
    print(Arr,K)
    Arr=mergeSort(Arr)
    print(Arr)
    left=0
    right=size-1
    while left<=right:
        sumOfTwo=Arr[left][0]+Arr[right][0]
        if sumOfTwo==K:
            return [Arr[left][1],Arr[right][1]]
        elif sumOfTwo<K:
            left+=1
        else:
            right-=1
    return None
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    leftArr=mergeSort(arr[:mid])
    rightArr=mergeSort(arr[mid:])
    return merge(leftArr,rightArr)
a1=testSet(10)
a2=testSet(20)
a3=testSet(40)
print(dual_sorted_search(a1,len(a1),a1[3]+a1[5],[]))

