#!/usr/bin/env python3

"""
Description of your project.
"""

import argparse


def main():
    print("Advent of Code 2024")
    #day01()
    day01_part2()

def day01():
    print("day 1 - attempt 1")
    #f = open("advent-2024-01-input.txt")
    f = open("advent-2024-01-input-small.txt")
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

def day01_part2():
    print("Day 01 - Part 2")
    f = open("advent-2024-01-input-small.txt")
    left_list = []
    right_list = []
    for x in f:
        one_line = x.split()
        left_list.append(one_line[0])
        right_list.append(one_line[1])

    similarity=0
    for x in left_list:
        dupe_count=0
        for y in right_list:
            if y==x:
                dupe_count+=1
                # print(dupe_count)
        print("There are " + str(dupe_count) + " occurrences of " + x)
        
    print(similarity)
    f.close

if __name__ == "__main__":
    main()