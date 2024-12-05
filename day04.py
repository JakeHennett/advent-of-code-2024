import sys
# sys.path.append('C:\\Users\\jakeh\\AppData\\Local\\Programs\\Python\\Python313\\Scripts')
#sys.path.append('C:\\Users\\jakeh\\AppData\\Local\\Programs\\Python\\*')
#import NumPy
#print(np.__version__)

def day04part1():
    print("day 4, part 1")
    # f = open("advent-2024-03-input.txt")
    f = open("advent-2024-04-input-small.txt")
    xmas_list=[]
    for x in f:
        xmas_list.append(x)
    xmas_count=0
    f.close
    print("XMAS count: " + str(xmas_count))

def day04part2():
    print("day 4, part 2")
    # f = open("advent-2024-03-input.txt")
    f = open("advent-2024-04-input-small.txt")
    f.close
    print("TODO")

if __name__ == "__main__":
    day04part1()
    day04part2()