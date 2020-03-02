import random

def find_min_max(arr, key):
    m = arr[0]
    for i in arr:
        if key == 'min':
            if i < m:
                m = i
        else:
            if i > m:
                m = i
    return m, arr.index(m)

arr = [random.randint(1, 100) for i in range(random.randrange(50))]
key = 'min'
print(arr)
print(find_min_max(arr, key))
