import math
import numpy as np

def day09part1():
    print("day 09, part 1")
    # file_name = "advent-2024-09-input-small.txt"
    # file_name = "advent-2024-09-input.txt"
    file_name = "advent-2024-09-input-reddit.txt"
    f = open(file_name)
    checksum=0
    string = f.read()
    input_array=list(string)
    # print(string)
    # print(input_array)
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
    # print(id_string)
    #00...111...2...333.44.5555.6666.777.888899

    # sorted_id_array=list(map(list, id_string))
    sorted_id_array=list(id_string)
    # print(sorted_id_array)
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
    print(''.join(sorted_id_array))


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

if __name__ == "__main__":
    day09part1()