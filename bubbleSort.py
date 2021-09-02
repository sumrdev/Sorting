import time
import random
def bubble(l):
    s = time.time()
    n = len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(l[j] > l[j+1]):
                h=l[j]
                l[j]=l[j+1]
                l[j+1]=h
    e = time.time()
    return l,e-s

def randomArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,1000))
    return arr

print(bubble(randomArr(100000)))