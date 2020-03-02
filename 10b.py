import matplotlib.pyplot as plt
from random import randrange

def insertionSort(alist):
    number_of_comparisions = 0
    number_of_swaps = 0
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            number_of_comparisions += 1
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
        number_of_swaps += 1
    return alist, number_of_comparisions, number_of_swaps

def mergeSort(alist, number_of_comparisions = 0, number_of_swaps = 0):
    if len(alist)>1:
        number_of_comparisions += 1
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            number_of_comparisions += 1
            if lefthalf[i]<righthalf[j]:
                number_of_comparisions += 1
                alist[k]=lefthalf[i]
                number_of_swaps += 1
                i=i+1
            else:
                alist[k]=righthalf[j]
                number_of_swaps += 1
                j=j+1
            k=k+1

        while i<len(lefthalf):
            number_of_comparisions += 1
            alist[k]=lefthalf[i]
            number_of_swaps += 1
            i=i+1
            k=k+1

        while j<len(righthalf):
            number_of_comparisions += 1
            alist[k]=righthalf[j]
            number_of_swaps += 1
            j=j+1
            k=k+1
    return alist, number_of_swaps, number_of_comparisions

def test(sort_func, n):
    test_metrics = []
    for i in range(n):
        arr = [randrange(500) for i in range(501)]
        results = sort_func(arr)
        test_metrics.append((results[1],results[2]))

    return test_metrics

insert_test_metrics = test(insertionSort, 10)
merge_test_metrics = test(mergeSort, 10)

num_comparisions_insert = [i[0] for i in insert_test_metrics]
num_swaps_insert = [i[1] for i in insert_test_metrics]

num_comparisions_merge = [i[0] for i in merge_test_metrics]
num_swaps_merge = [i[1] for i in merge_test_metrics]

x = len(insert_test_metrics)
width = 0.5

labels = ['сортировка вставками', 'сортировка слиянием']

#plots
fig, ax = plt.subplots(1, 2, figsize=(10, 8))

ax[0].set_title('Количество сравнений')
ax[0].bar(labels[0],num_comparisions_insert, width, label=labels[0])
ax[0].bar(labels[1],num_comparisions_merge, width, label=labels[1])
ax[0].legend()

ax[1].set_title('Количество перестановок')
ax[1].bar(labels[0],num_swaps_insert, width, label=labels[0])
ax[1].bar(labels[1],num_swaps_merge, width, label=labels[1])
ax[1].legend(loc='upper left')


plt.show()
