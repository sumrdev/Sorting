import random
import time
import sys
sys.setrecursionlimit(1500)
def quickSort(s):
    length = len(s)
    if length <= 1:
        return s
    else:
        pivot = s.pop()
    
    g = []
    l = []
    
    for x in s:
        if x > pivot:
            g.append(x)
        else:
            l.append(x)
    return quickSort(l) + [pivot] + quickSort(g)

def randomArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,1000))
    return arr

def timeChecker():
    s = time.time()
    sorted = quickSort(randomArr(1000000))
    e = time.time()
    return e-s

print("quickSort " , timeChecker())