#!/usr/bin/env python3

"""
Description of your project.
"""

import argparse


def main():
    print("Advent of Code 2024")
    #day01()
    #day01_part2()
    #day02()
    day02part2()

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
    #f = open("advent-2024-01-input-small.txt")
    f = open("advent-2024-01-input.txt")
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
        #print("There are " + str(dupe_count) + " occurrences of " + x)
        similarity+=(dupe_count * int(x))
        #print(similarity)
        
    print(similarity)
    f.close

def day02():
    print("day 2")
    f = open("advent-2024-02-input.txt")
    # f = open("advent-2024-02-input-small.txt")
    safe_count=0
    for x in f:
        # print(x)
        my_list=x.split()
        direction = []
        difference = []
        for y in range(len(my_list)-1):
            first = int(my_list[y])
            second = int(my_list[y+1])
            if (first < second):
                direction.append("Up")
            else:
                direction.append("Down")
            difference.append(abs(second-first))
            # print(direction[y] + " " + str(difference[y]))

        unidirectional=True
        gradual=True
        if (direction.__contains__("Up") and direction.__contains__("Down")):
            unidirectional=False
            # print("both ways")
        for y in difference:
            # print(y)
            if y<1:
                gradual=False
                # print("too low")
            if y>3:
                gradual=False
                # print("too high")
        
        if (unidirectional and gradual):
            safe_count+=1
    
    print(safe_count)

    #close file
    f.close()

def day02part2():
    print("day 2 part 2")
    f = open("advent-2024-02-input.txt")
    # f = open("advent-2024-02-input-small.txt")
    safe_count=0
    for x in f:
        # print(x)
        my_list=x.split()
        #TODO: Replace this logic with a method call
        direction = []
        difference = []
        for y in range(len(my_list)-1):
            first = int(my_list[y])
            second = int(my_list[y+1])
            if (first < second):
                direction.append("Up")
            else:
                direction.append("Down")
            difference.append(abs(second-first))
            # print(direction[y] + " " + str(difference[y]))

        unidirectional=True
        gradual=True
        if (direction.__contains__("Up") and direction.__contains__("Down")):
            unidirectional=False
            # print("both ways")
        for y in difference:
            # print(y)
            if y<1:
                gradual=False
                # print("too low")
            if y>3:
                gradual=False
                # print("too high")
        
        if (unidirectional and gradual):
            safe_count+=1
        else:
            # print("check sublists")
            safe_sublist=False
            # print(my_list)
            for y in range(len(my_list)):
                # print("index " + str(y) + " is " + my_list[y])
                sub_list=list(my_list)
                del sub_list[y]
                # print(sub_list)
                #loop to apply the same logic to each sublist and see if any are safe
                # TODO: replace this logic with a method call

                sub_direction = []
                sub_difference = []
                for sub_y in range(len(sub_list)-1):
                    sub_first = int(sub_list[sub_y])
                    sub_second = int(sub_list[sub_y+1])
                    if (sub_first < sub_second):
                        sub_direction.append("Up")
                    else:
                        sub_direction.append("Down")
                    sub_difference.append(abs(sub_second-sub_first))
                    # print(direction[y] + " " + str(difference[y]))

                sub_unidirectional=True
                sub_gradual=True
                if (sub_direction.__contains__("Up") and sub_direction.__contains__("Down")):
                    sub_unidirectional=False
                    # print("both ways")
                for sub_y in sub_difference:
                    # print(y)
                    if sub_y<1:
                        sub_gradual=False
                        # print("too low")
                    if sub_y>3:
                        sub_gradual=False
                        # print("too high")

                if (sub_unidirectional and sub_gradual):
                    safe_sublist=True
                #end recreated logic
            if safe_sublist:
                # print("a sublist was safe")
                safe_count+=1
    
    print(safe_count)

    #close file
    f.close()

if __name__ == "__main__":
    main()