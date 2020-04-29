import profile

'''
Чи́сла трибона́ччи — последовательность целых чисел N, 
заданная с помощью линейного рекуррентного соотношения.

Первые три числа всегда равны:
t0 = 0, t1 = 0, t2 = 1 

Последовательность чисел трибоначчи начинается так:
0, 0, 1, 1, 2, 4...
'''

# Regular implementation of Tribonacci sequence
def trib(n):
    if n <= 2: 
        return 0
    elif n == 3: 
        return 1
    else: 
        return trib(n - 1) + trib(n - 2) + trib(n - 3)

# Optimized version. 
# Storing all previously computed values in memo(cache)
# and later using them to calculated values
def tribOpt(n, memo=[]):
    # values that always return zero
    if n <= 2: 
        return 0
    elif n == 3: 
        return 1
    elif memo[n] > 0:
        return memo[n]
    else:
        memo[n] = tribOpt(n - 1, memo) + tribOpt(n - 2, memo) + tribOpt(n - 3, memo)
    return memo[n]

# Print first N numbers of the sequence
def printResults(n):
    memo = [0]*(n+1)
    print("The first {} numbers of Tribonacchi sequence is: ".format(n), end="")
    for i in range(1, n+1):
        print(tribOpt(i, memo), " ", end="")

# funtions for running tests
def testRegularTrib(n):
    for i in range(1, n+1) : 
        trib(i)

def testOptimizedTrib(n):
    memo = [0]*(n+1)
    for i in range(1, n+1):
        tribOpt(i, memo)

# results
printResults(10)

# Test. What is faster ?
# Value for testing purposes only 
N = 20
print("")
print("\nTest results: ")
print("Regular Tribonacci funtion: ")
profile.runctx('testRegularTrib(n)', globals(), {'n': N})
print("Optimized Tribonacci function: ")
profile.runctx('testOptimizedTrib(n)', globals(), {'n': N})