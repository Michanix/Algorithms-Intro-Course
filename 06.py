import sys

def fn(x):
    return x**2


eps = sys.float_info.epsilon
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 34, 43, 56]


def golden_search(arr, func, key, fi=1.618):
    a = arr[0]
    b = arr[-1]
    x = 0
    x1 = b - (b-a)//fi
    x2 = a + (b-a)//fi
    y1 = func(x1)
    y2 = func(x2)
    while True:       
        if abs(b-a) < eps:
            x = (a+b)/2
            break
        if key == 'min':  
            if y1 >= y2:
                a = x1
            else:
                b = x2
        else:
            if y1 <= y2:
                a = x1
            else:
                b = x2
        x1 = b - (b-a)//fi
        x2 = a + (b-a)//fi
    return x

print(golden_search(arr, fn, 'max'))
