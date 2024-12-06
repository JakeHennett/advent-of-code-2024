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

    #find guard and create object
    guard_x = 0
    guard_y = 0
    #TODO: check these axes
    for x in range(map_array.shape[0]):
        for y in range(map_array.shape[1]):
            if (map_array[x][y]=='^'):
                guard_x=y
                guard_y=x
    guard1 = Guard(guard_x, guard_y, 'N')
    print(guard1.display())
    guard1.walk()
    print(guard1.display())
    guard1.turn()
    print(guard1.display())
    guard1.walk()
    print(guard1.display())

    guard_path = map_array

class Guard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def turn(self):
        if (self.direction=='N'):
            self.direction='E'
        elif (self.direction=='E'):
            self.direction='S'
        elif (self.direction=='S'):
            self.direction='W'
        elif (self.direction=='W'):
            self.direction='N'
        else:
            self.direction='N'  #reset unknown direction to N
    
    def walk(self):
        if (self.direction=='N'):
            self.y-=1
        elif (self.direction=='E'):
            self.x+=1
        elif (self.direction=='S'):
            self.y+=1
        elif (self.direction=='W'):
            self.x-=1
        else:
            #reset unknown position to out of bounds
            self.x=-1
            self.y=-1
    
    def display(self):
        status = "Guard is at (" + str(self.x) + ", " + str(self.y) + "), facing " + self.direction
        return status
    
if __name__ == "__main__":
    day06part1()