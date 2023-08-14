'''
test_important.py: Script to test the pytest fixture which has been introduced in the file conftest.py
Author: Abhirup Gupta
'''

import sys
import os.path
path = os.path.abspath(__file__)
source_code_location = os.path.dirname(os.path.dirname(path))
sys.path.append(source_code_location + "/src/")
from static_methods import Task

def get_sum(a):
    return sum(a)

def test_if_important(important_value):
    assert important_value == True

def test_get_sum(int_list):
    assert get_sum(int_list) == 10

# here, we are adding the test for the Static method
def test_static_methods():
    assert Task.get_cube(3) == 27
    assert Task.get_square(2) == 4

