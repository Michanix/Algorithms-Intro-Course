from random import randint
from random import randrange
from time import time
# O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                # меняем элементы местами
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

test1 = [randint(0, 10) for x in range(1, 10)]

print("Обычный пузырёк: ")
print(test1)
start = time()
print(bubble_sort(test1))
end = time()
print(end - start)


