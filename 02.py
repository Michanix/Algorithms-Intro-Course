from random import randint

def find_max_indx(arr):
    m = arr[0]
    for i in arr:
        if i > m:
            m = i
    return arr.index(m)

def acs_sort(arr, arr2=[]):
    if arr == []:
        return arr2[::-1]
    m = find_max_indx(arr)
    arr[m], arr[-1] = arr[-1], arr[m]
    arr2 += [arr[-1]]
    return acs_sort(arr[:-1])

a = [randint(1, 101) for i in range(11)]
print(a)
print(acs_sort(a))