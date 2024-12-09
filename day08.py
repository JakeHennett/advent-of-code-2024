import math
import numpy as np

def day08part1():
    print("day 08, part 1")
    file_name = "advent-2024-08-input-small.txt"
    # file_name = "advent-2024-08-input.txt"
    map_file = open(file_name)
    string_array=[]
    #iterate over file to find line count and line length
    for line in map_file:
        string_array.append(line.rstrip())
    map_file.close

    map_array = np.array(list(map(list, string_array)))
    print(map_array)

    #generate a list of all unique antenna types
    antenna_list = []
    for x in range(map_array.shape[0]):
        for y in range(map_array.shape[1]):
            antenna=map_array[x][y]
            # print(antenna)
            if (antenna!='.' and antenna_list.count(antenna) == 0):
                antenna_list.append(str(antenna))
    print(antenna_list)
    
if __name__ == "__main__":
    day08part1()