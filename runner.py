import xlsxwriter
from bubbleSort import *
from selectionSort import *
from mergeSort import *
from quickSort import *

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()
algos = ['Bubblesort', 'Selectionsort', 'Mergesort', 'Quicksort']
a = [bubbleSortTester,selectionSortTester,mergeSortTester,quickSortTester]
arrayTypes = ['nearly sorted','few unique','random','reverse']
for c in range(1,5):
    worksheet.write(2,c*6-4, algos[c-1])
    worksheet.write(3,c*6-4, 'n')
    for i in range(0,4):
        worksheet.write(3,c*6+i-3, arrayTypes[i])    

for r in range(10):
    for c in range(4):
        for i in range(4):
            worksheet.write(r+4,(c*6)+3+i,a[c](1000*r,arrayTypes[i]))
            worksheet.write(r+4,c*6+2,pow(10,r+1))
            print(i,c,r)
workbook.close()