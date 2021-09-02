def selectionSort(arr):
    for i in range(len(arr)-2):
        if arr[i] > arr[len(arr)-1]:
            h = arr[i]
            arr[i] = arr[len(arr)-1]
            arr[len(arr)-1] = h
    return arr

print(selectionSort([5,4,3,2,1]))