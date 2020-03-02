import matplotlib.pyplot as plt
import numpy as np
from math import ceil
from time import time
from random import randint, randrange


def bin_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low != high:
        mid = ceil((low + high)/2)
        if arr[mid]  == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    if arr[low] == key:
        return low
    return None

times = []
elements = []

arr_lengths = [10, 100, 1000, 10000, 10**6, 10**7, 10**8]
xlabels = ['10', '10^2', '10^3', '10^4', '10^5', '10^6', '10^7', '10^8']
for i in arr_lengths:
    arr = [j for j in range(i)]

    start = time()
    v = bin_search(arr, randrange(i))
    end = time() - start
    print(v)
    
    elements.append(len(arr))
    times.append(end)
    
plt.xticks(np.arange(len(elements)), xlabels)
plt.plot(np.arange(len(elements)), times, 'o-')
plt.show()