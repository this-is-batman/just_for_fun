'''
This code deals with profiling the memory requirements for a certain piece of code
'''

from memory_profiler import profile

@profile
def process_strs(reps = 10**4):
    str1 = "python" * reps
    str2 = "programmer" * reps
    str3 = str1 + str2
    del str2
    return str3

process_strs(reps = 10**1) 