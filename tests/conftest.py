'''
conftest.py: Common configuration file which can be used for running unit tests
Author: Abhirup Gupta
'''

# this file named conftest.py contains fixtures that can be used across multiple files
import pytest

@pytest.fixture
def important_value():
    important = True
    return important

@pytest.fixture
def int_list():
    return [1,2,3,4]


