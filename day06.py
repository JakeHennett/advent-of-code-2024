import math
import numpy as np

def day06part1():
    print("day 6, part 1")
    file_name = "advent-2024-06-input-small.txt"
    map_file = open(file_name)
    #input_file = open("advent-2024-06-input-small.txt")
    #rules_file = open("advent-2024-06-rules-small.txt")
    line_count=0
    character_count=0
    string_array=[]
    #iterate over file to find line count and line length
    for line in map_file:
        string_array.append(line)
        line_count+=1
        character_count=len(line)
        print(line)
    #size of array has been found
    print("Array will be " + str(line_count) + " by " + str(character_count))
    print(string_array)
    map_file.close

    map_array = np.zeros(shape=(line_count,character_count))
    #map_array = np.array(list(map(list, string_array)))
    print(map_array)
    
    map_file = open(file_name)
    line_count=0
    character_count=0
    #iterate over file to populate array
    for line in map_file:
        #print(line)
        for character in line:
            print("Character at " + str(line_count) + ", " + str(character_count) + " is " + character)
            #map_array[line_count][character_count]=character
            character_count+=1
        line_count+=1
        character_count=0
    print(map_array)

    map_file.close

if __name__ == "__main__":
    day06part1()