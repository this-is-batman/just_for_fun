'''
test_important.py: Script to test the pytest fixture which has been introduced in the file conftest.py
Author: Abhirup Gupta
'''

import pytest

def get_sum(a):
    return sum(a)

def test_if_important(important_value):
    assert important_value == True

def test_get_sum(int_list):
    assert get_sum(int_list) == 10
