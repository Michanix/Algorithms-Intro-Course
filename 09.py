from random import randrange
from time import time


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                # меняем элементы местами
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


def opt_bubble_sort(arr):
    while True:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        if not swap:
            break

        swap = False

        for j in range(len(arr)-1, 0):
            if arr[j] < arr[j+1]:
                # меняем элементы местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
    return arr

# измерить время работы алгоритма в случайом массиве

def check_time_in_random_arr(f):
    arr = [randrange(100) for i in range(1100)]
    start = time()
    f(arr)
    end = time()
    return end - start

# время работы алгоритма в сортированном массиве

def check_time(f):
    arr = [i for i in range(1100)]
    start = time()
    f(arr)
    end = time()
    return end - start


bubble_sort_time = check_time(bubble_sort)
opt_bubble_sort_time = check_time(opt_bubble_sort)
bubble_sort_time2 = check_time_in_random_arr(bubble_sort)
opt_bubble_sort_time2 = check_time_in_random_arr(opt_bubble_sort)

print('''
    Время работы в уже отсортированном массиве:\n
    Обычный пузырёк: {}\n
    Модифицированный {}\n
    Время работы в случайном массиве: \n
    Обычный пузырёк: {}\n
    Модифицированный: {}'''.format(bubble_sort_time, opt_bubble_sort_time, bubble_sort_time2, opt_bubble_sort_time2))
