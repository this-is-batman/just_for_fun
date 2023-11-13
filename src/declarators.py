'''
declarators.py: Script to test out some declarators to enhance the abilities of functions in python
'''
import time
from typing import List

def compute_time(func):
    """
    a python declarator which adds the timing required to run any function
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(f"Time required to run the function {func.__name__} is {end - start}.")
        return f
    return wrapper 

@compute_time
def get_sum(a: int,b: int) -> int:
    """
    get the sum of two numbers
    """
    return a + b

@compute_time
def get_diff(a: int, b: int) -> int:
    """
    get the difference of two numbers
    """    
    return a - b


@compute_time
def get_sum_list(l1: List[int], l2: List[int]) -> List[int]:
    """
    get the sum of two lists of integers
    """
    assert len(l1) == len(l2)
    sum_list = []
    for idx, i in enumerate(l1):
        sum_list.append(i + l2[idx])
    return sum_list

@compute_time
def get_sum_list_opt(l1: List[int], l2: List[int]) -> List[int]:
    """
    get the sum of two lists of integers using python in built list addition
    """
    assert len(l1) == len(l2)
    sum_list = l1 + l2
    return sum_list
    

# this statement should always be true
assert get_sum_list([1,2], [3,4]) >= get_sum_list_opt([1,2], [3,4])
