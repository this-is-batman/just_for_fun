'''
static_methods.py: Script to understand more about static methods in python
For more information visit https://www.geeksforgeeks.org/class-method-vs-static-method-python/
Author: Abhirup Gupta
'''

class Task:
    @staticmethod
    def get_square(x: int) -> int:
        """function to get the square of a number

        Args:
            x (int): input

        Returns:
            int: square of the output
        """
        return x**2
    
    def get_cube(x: int) -> int:
        '''
        not giving description
        '''
        return x**3


if __name__ == '__main__':
    assert Task.get_square(4) == 16
    assert Task.get_cube(3) == 27