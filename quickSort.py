import time
import sys
from Array_Generator import *
sys.setrecursionlimit(999999)
def quickSort(s):
    length = len(s)
    if length <= 1:
        return s
    pivot = s.pop()
    
    g = []
    l = []
    
    for x in s:
        if x > pivot:
            g.append(x)
        else:
            l.append(x)
    return quickSort(l) + [pivot] + quickSort(g)

def quickSortTester(n, arrayType):
    a = genArr(n,arrayType)
    s = time.time()
    sorted = quickSort(a)
    e = time.time()
    return e-s

print(quickSortTester(100000,'few unique'))