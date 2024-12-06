import math
import numpy as np

def day06part1():
    print("day 6, part 1")
    file_name = "advent-2024-06-input-small.txt"
    map_file = open(file_name)
    string_array=[]
    #iterate over file to find line count and line length
    for line in map_file:
        string_array.append(line.rstrip())
    map_file.close

    map_array = np.array(list(map(list, string_array)))
    print(map_array)

if __name__ == "__main__":
    day06part1()