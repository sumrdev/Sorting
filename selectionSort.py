import time
import random
def selectionSort(l):
    s = time.time()
    for i in range(len(l)-1):
        min = i
        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                min = j
        if min != i:
            h = l[i]
            l[i] = l[min]
            l[min] = h
    e = time.time()
    return e-s

def randomArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,1000))
    return arr
print("SelectionSort " , selectionSort(randomArr(100000)))