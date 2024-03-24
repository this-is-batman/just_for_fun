"""
This script contains the code required to time a module using profiler
"""

import pstats
import time
import cProfile

def func(num):
    for i in range(num):
        print(i)

def another_func(num):
    time.sleep(num)
    print(f"Slept for {num} seconds.")

def useful_func(nums, target):
    if target in nums:
        return nums.index(target)

if __name__ == "__main__":
    with cProfile.Profile() as profile:
        func(1000)
        another_func(5)
        useful_func([2,8,12,4], 12)
    profile_result = pstats.Stats(profile)
    profile_result.sort_stats(pstats.SortKey.TIME)
    profile_result.print_stats()