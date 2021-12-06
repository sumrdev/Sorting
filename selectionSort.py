import time
from Array_Generator import *
def selectionSort(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                min = j
        if min != i:
            h = l[i]
            l[i] = l[min]
            l[min] = h
    return l

def selectionSortTester(n,arrayType):
    a = genArr(n,arrayType)
    s = time.time()
    sorted = selectionSort(a)
    e = time.time()
    return e-s
