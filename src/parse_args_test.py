'''
parse_ags_test: Script to test command line argument parser in python
Author: Abhirup Gupta
'''
import argparse

def parse_args():
    '''
    parse_args: Function to parse the command line arguments
    Input: None
    OUtput: Returns a parser object
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type = int, help="value of the first argument.", default=3)  # these are optional arguments
    parser.add_argument("--y", type = int, help="value of the second argument.", default = 3)  # these are optional arguments
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()  # this is the parser object
    if args.x is None or args.y is None:
        raise SyntaxError("Type --help to see how you can correctly ecxecute the code.")
    print(args.x * args.y)
