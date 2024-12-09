import math
import numpy as np

def day09part1():
    print("day 09, part 1")
    file_name = "advent-2024-09-input-small.txt"
    # file_name = "advent-2024-09-input.txt"
    # file_name = "advent-2024-09-input-reddit.txt"
    f = open(file_name)
    checksum=0
    string = f.read()
    input_array=list(string)
    # print(string)
    # print(input_array)
    id_string = ""
    id_array = []
    data = []
    gaps = []
    for x in range(len(input_array)):
        item_size=-1
        try:
            item_size=int(input_array.__getitem__(x))
        except:
            item_size=0
        
        if (x % 2 == 0):
            one_file = DataFile(int(np.floor(x/2)),input_array.__getitem__(x))
            data.append(one_file)
        else:
            gaps.append(input_array.__getitem__(x))
        
        file_item=""
        # file_item_array=[]
        for y in range(item_size):
            if (x % 2 == 0):
                file_id = int(np.floor(x / 2))
                file_item+=str(file_id)
                # file_item_array.append(file_id)
                id_array.append(str(file_id))
            else:
                file_item+='.'
                # file_item_array.append('.')
                id_array.append('.')
        id_string+=file_item
        # id_array.append
    # print(id_string)
    #00...111...2...333.44.5555.6666.777.888899
    print(id_array)
    # print(data)
    for x in data:
        print(x.display())
    print(gaps)


    print(defrag(data, gaps))
    print(simpleDefrag(id_array, gaps))

    sorted_id_array=id_array
    is_sorted=False
    # reverse_id_iterator=int(id_string.__len__())
    reverse_id_iterator=int(sorted_id_array.__len__())
    while (not is_sorted):
        # is_sorted=True
        # first_blank=id_string.find('.') #change to array
        try:
            first_blank=sorted_id_array.index('.')
        except:
            first_blank=sorted_id_array.__len__()
        # print("First blank at index: " + str(first_blank))
        last_char="."
        while (last_char=="."):
            reverse_id_iterator-=1
            # print("Stepping back through array at index " + str(reverse_id_iterator))
            # last_char=id_string.__getitem__(reverse_id_iterator) #change to array
            last_char=sorted_id_array.__getitem__(reverse_id_iterator)
        if(first_blank > reverse_id_iterator):
            is_sorted=True
        else:
            sorted_id_array[first_blank]=last_char
            sorted_id_array[reverse_id_iterator]='.'
        # print("Last valid character is " + last_char)
        # print("After sorting, array looks like this:")
        # print(sorted_id_array)
        # if((first_blank+1) >= (reverse_id_iterator-1)):
        #     is_sorted=True
    # print(sorted_id_array)
    # print(sorted_id_array)
    # print(''.join(sorted_id_array))

    #find checksum
    array_iter=0
    for x in sorted_id_array:
        try:
            individual_sum=(int(x) * array_iter)
        except:
            individual_sum=0
        array_iter+=1
        checksum+=individual_sum
    print(checksum)
    #89403351457 too low
    #89403351449 too low
    #6258319840548

def defrag(data, gaps):
    print("Defragmenting drive...")
    defrag_checksum=0
    sorted_defrag=data
    reduced_gaps=gaps
    new_combined_array=[data[0].length]
    for x in data:
        # print(x.display())
        for y in gaps:
            # print(y)
            if(x.length <= y):
                # print("gap is large enough for file")
                new_combined_array.append(x)
    # print(new_combined_array)

    return defrag_checksum

def simpleDefrag(id_array, gaps):
    print("Defragmenting drive...")
    print(id_array)
    defrag_checksum=0
    gap_index=0
    unique_id_count=int(id_array.__getitem__(id_array.__len__()-1))
    print(unique_id_count)
    for i in range(unique_id_count, 0, -1):
        print(i)
        file_size=id_array.count(str(i))
        print(file_size)
        gap_index=0
        for j in range(unique_id_count):
            gap_start=id_array.index('.', gap_index)
            gap_size=int(gaps[j])
            print("Gap starts at " + str(gap_start) + " for a length of " + str(gap_size))
            gap_index= gap_index + gap_size

    return defrag_checksum

class DataFile:
    def __init__(self, id, length):
        self.id = id
        self.length = length

    def display(self):
        return "(" + str(self.id) + "," + str(self.length) + ")"

if __name__ == "__main__":
    day09part1()