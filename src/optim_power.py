'''
This is a very important script showing the power of optimization
Author: Abhirup Gupta
'''

from tqdm import tqdm
import matplotlib.pyplot as plt
import time

def get_square(x: int) -> int:
    return x**2


def get_fib(n: int) -> int:
    '''
    get_fib: Unoptimized version of getting the fibonacci value for a certain value of n 
    Input: n
    return: Fibonacci(n)
    '''
    if n in [0,1]:
        return n
    else:
        return get_fib(n-1) + get_fib(n -2)
    

def get_fib_opt(n: int, fib_dict: dict) -> int:
    '''
    get_fib_opt: Optimized version of getting the fibonacci value for a certain value of n
    Input: n
    return: Fibonacci(n)
    '''
    if n in fib_dict:
        return fib_dict[n]
    for i in range(2,n+1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
    return fib_dict[n]

if __name__ == '__main__':   # this is done so that this part of the script is not run during import
    times_optimized = []
    times_unoptimized  = []

    for num_iters in tqdm(range(1,41)):
        start = time.time()
        get_fib(num_iters)
        end = time.time()
        times_unoptimized.append(end - start)

    fib_dict = {}
    fib_dict[0] = 0
    fib_dict[1] = 1
    for num_iters in tqdm(range(1,41)):
        start = time.time()
        get_fib_opt(num_iters, fib_dict)
        end = time.time()
        times_optimized.append(end - start)

    # here, we are plotting the time required to return results from the optimized code and return results from the unoptimized code
    # thus, we can see the differences between the optimized implementation and the unoptimized representation in graphical format.
    plt.plot(times_unoptimized, "g", times_optimized, "r")
    plt.show()
