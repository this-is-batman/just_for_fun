'''
test_fib.py: Script to test the correctness of the fibonacci function present in the /src/ directory
Author: Abhirup Gupta
'''

import sys
import os.path
path = os.path.abspath(__file__)
source_code_location = os.path.dirname(os.path.dirname(path))
sys.path.append(source_code_location + "/src/")
from optim_power import get_fib, get_fib_opt

fib_dict = {}
fib_dict[0] = 0
fib_dict[1] = 1

def test_fib() -> int:
    assert get_fib(1) == 1
    assert get_fib_opt(3, fib_dict) == 3
