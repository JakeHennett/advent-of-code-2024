#!/usr/bin/env python3

"""
Description of your project.
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Description of your script.")
    # Add arguments here if needed
    # parser.add_argument('-f', '--file', help='File to process', required=True)
    args = parser.parse_args()

    # Your main logic here
    print("hello world")
    day01()

def day01():
    print("day 1 - attempt 1")
    f = open("advent-2024-01-input.txt")
    left_list = []
    right_list = []
    for x in f:
        one_line = x.split()
        left_list.append(one_line[0])
        right_list.append(one_line[1])
    
    left_list.sort()
    right_list.sort()

    total_difference=0
    for x in range(len(left_list)):
        left=int(left_list[x])
        right=int(right_list[x])
        total_difference+=abs(left-right)
        #debug print(total_difference)
    
    print(total_difference)

    #close file
    f.close()

if __name__ == "__main__":
    main()