import math
import numpy as np

def day09part1():
    print("day 09, part 1")
    file_name = "advent-2024-09-input-small.txt"
    # file_name = "advent-2024-09-input.txt"
    f = open(file_name)
    checksum=0
    input_array = []
    string = f.read()
    for x in range(len(string)):
        input_array.append(string.__getitem__(x))
    print(string)
    print(input_array)
    id_string = ""
    for x in range(len(input_array)):
        item_size=-1
        try:
            item_size=int(input_array.__getitem__(x))
        except:
            item_size=0
        
        file_item=""
        for y in range(item_size):
            if (x % 2 == 0):
                file_id = int(np.floor(x / 2))
                file_item+=str(file_id)
            else:
                file_item+='.'
        id_string+=file_item
    print(id_string)
    print(checksum)

if __name__ == "__main__":
    day09part1()