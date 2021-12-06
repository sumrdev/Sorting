import time
from Array_Generator import *
def bubble(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(l[j] > l[j+1]):
                h=l[j]
                l[j]=l[j+1]
                l[j+1]=h
    return l

def bubbleSortTester(n,arrayType):
    a = genArr(n,arrayType)
    s = time.time()
    sorted = bubble(a)
    e = time.time()
    return e-s
