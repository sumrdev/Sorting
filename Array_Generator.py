import random

def genArr(iterations,arrType):
    if arrType == 'random':
        return randomArr(iterations)
    if arrType == 'reverse':
        return reverseArr(iterations)
    if arrType == 'few unique':
        return fewUniqueArr(iterations)
    if arrType == 'nearly sorted':
        return nearlySortedArr(iterations)

def randomArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,1000))
    return arr

def reverseArr(iterations):
    arr = []
    for i in range(iterations,0,-1):
        arr.append(i)
    return arr

def fewUniqueArr(iterations):
    arr = []
    for i in range(iterations):
        arr.append(random.randint(0,100))
    return arr

def nearlySortedArr(iterations):
    arr = []
    for i in range(iterations):
        x = random.randint(0,10)
        if x == 0:
            arr.append(random.randint(0,iterations))
        else: arr.append(i)
    return arr
