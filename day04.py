import sys
import numpy as np
# sys.path.append('C:\\Users\\jakeh\\AppData\\Local\\Programs\\Python\\Python313\\Scripts')
#sys.path.append('C:\\Users\\jakeh\\AppData\\Local\\Programs\\Python\\*')
#import NumPy
#print(np.__version__)

def day04part1():
    print("day 4, part 1")
    xmas_count=0
    file_name = "advent-2024-04-input-small.txt"
    #file_name = "advent-2024-04-input.txt"
    xmas_list_file = open(file_name)
    string_array=[]
    #iterate over file to find line count and line length
    for line in xmas_list_file:
        string_array.append(line.rstrip())
    xmas_list_file.close

    xmas_list = np.array(list(map(list, string_array)))

    print(xmas_list)

    for x in range(xmas_list.shape[0]):
        for y in range(xmas_list.shape[1]):
            if (xmas_list[x][y]=='X'):
                print(str(x) + ", " + str(y))
                local_count=checkSpot(x, y, xmas_list)
                xmas_count+=local_count

    print("XMAS count: " + str(xmas_count))

def checkSpot(x, y, xmas_list):
    print(str(x) + ", " + str(y))
    word_count=0
    #check N
    try:
        if (xmas_list[x][y+1] == 'M'):
            print("Second letter M")
            if (xmas_list[x][y+2] == 'A'):
                print("Third letter A")
                if (xmas_list[x][y+3] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check NE
    try:
        if (xmas_list[x+1][y+1] == 'M'):
            print("Second letter M")
            if (xmas_list[x+2][y+2] == 'A'):
                print("Third letter A")
                if (xmas_list[x+3][y+3] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check E
    try:
        if (xmas_list[x+1][y] == 'M'):
            print("Second letter M")
            if (xmas_list[x+2][y] == 'A'):
                print("Third letter A")
                if (xmas_list[x+3][y] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check SE
    try:
        if (xmas_list[x-1][y+1] == 'M'):
            print("Second letter M")
            if (xmas_list[x-2][y+2] == 'A'):
                print("Third letter A")
                if (xmas_list[x-3][y+3] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check S
    try:
        if (xmas_list[x-1][y] == 'M'):
            print("Second letter M")
            if (xmas_list[x-2][y] == 'A'):
                print("Third letter A")
                if (xmas_list[x-3][y] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check SW
    try:
        if (xmas_list[x-1][y-1] == 'M'):
            print("Second letter M")
            if (xmas_list[x-2][y-2] == 'A'):
                print("Third letter A")
                if (xmas_list[x-3][y-3] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check W
    try:
        if (xmas_list[x-1][y] == 'M'):
            print("Second letter M")
            if (xmas_list[x-2][y] == 'A'):
                print("Third letter A")
                if (xmas_list[x-3][y] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    #check NW
    try:
        if (xmas_list[x-1][y+1] == 'M'):
            print("Second letter M")
            if (xmas_list[x-2][y+2] == 'A'):
                print("Third letter A")
                if (xmas_list[x-3][y+3] == 'S'):
                    print("Fourth letter S")
                    word_count+=1
    except:
        word_count+=0
    return word_count

def day04part2():
    print("day 4, part 2")
    # f = open("advent-2024-03-input.txt")
    f = open("advent-2024-04-input-small.txt")
    f.close
    print("TODO")

if __name__ == "__main__":
    day04part1()
    day04part2()