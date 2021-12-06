from Array_Generator import *
import time
import sys
def quick3(arr):

    if len(arr) <= 1:
        return arr

    left_pivot = arr[0]
    right_pivot = arr.pop()

    if left_pivot > right_pivot:
        left_pivot, right_pivot = right_pivot, left_pivot

    left = []
    mid = []
    right = []
    
    for i in arr:
        if i < left_pivot: left.append(i)
        elif i > left_pivot and i < right_pivot: mid.append(i)
        elif i < right_pivot: right.append(i)
    return quick3(left) + [left_pivot] + quick3(mid) + [right_pivot] + quick3(right)


def quickSortTester(n, arrayType):
    a = genArr(n,arrayType)
    s = time.time()
    sorted = quick3(a)
    e = time.time()
    return e-s

print(quickSortTester(100000,'few unique'))