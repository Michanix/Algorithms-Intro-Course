import matplotlib.pyplot as plt
import numpy as np
from time import time
from random import randrange


def partition(a, low, high):
    i = low+1
    pivot = randrange(low, high+1)
    a[low], a[pivot] = a[pivot], a[low]

    for j in range(low+1, high+1):
        if a[j] < a[low]:
            a[i], a[j] = a[j],a[i]
            i += 1
    a[low],a[i-1] = a[i-1],a[low]
    return i - 1

def quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quicksort(a, low, p - 1)
        quicksort(a, p+1, high)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                # меняем элементы местами
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


lengths = [5000, 10000, 20000, 30000]
xlabels = [str(i) for i in lengths]
quick_times = []
bubble_times = []
for i in lengths:
    x = [randrange(i+1) for i in range(i)]

    start = time()
    quicksort(x, 0, len(x)-1)
    end = time() - start
    quick_times.append(end)

for i in lengths:
    x = [randrange(i+1) for i in range(i)]

    start = time()
    bubble_sort(x)
    end = time() - start
    bubble_times.append(end)


plt.xticks(np.arange(len(lengths)), xlabels)
plt.plot(np.arange(len(lengths)), quick_times, 'ob-')
plt.plot(np.arange(len(lengths)), bubble_times, 'or-')
plt.legend(['Быстрая сортировка','Пузырёк'])
plt.grid(True)
plt.show()