import random
import time


def arrayGen(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,n-1))
    return arr


def bucketSort(arr):
    buckets = maxNumber(arr)
    finished = []
    print(len(buckets),len(arr))
    for i in range(len(arr)):
        buckets[arr[i]]+=1
    for i in range(len(buckets)):
        for j in range(buckets[i]):
            finished.append(i)
    return finished

def maxNumber(arr):
    l = 0
    n = []
    for i in range(len(arr)):
        if arr[i] > l: l = arr[i]
    for i in range(len(arr)):
        n.append(0)
    return n

def tester(n):
    s = time.time()
    a = bucketSort(arrayGen(n))
    e = time.time()
    return e-s

print(tester(10000000))

