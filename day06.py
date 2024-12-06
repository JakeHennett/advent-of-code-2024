import math
import numpy as np

def day06part1():
    print("day 6, part 1")
    #file_name = "advent-2024-06-input-small.txt"
    file_name = "advent-2024-06-input.txt"
    map_file = open(file_name)
    string_array=[]
    #iterate over file to find line count and line length
    for line in map_file:
        string_array.append(line.rstrip())
    map_file.close

    map_array = np.array(list(map(list, string_array)))
    
    #find infinite loops
    print("Possible infinite loops: " + str(findLoops(map_array)))

    #print(map_array)
    #print(map_array.shape)

    #find guard and create object
    guard_x = 0
    guard_y = 0
    obstacle_list = []
    #TODO: check these axes
    for x in range(map_array.shape[0]):
        for y in range(map_array.shape[1]):
            if (map_array[x][y]=='^'):
                guard_x=y
                guard_y=x
            elif (map_array[x][y]=='#'):
                obstacle_list.append(Obstacle(y,x))
                #print(obstacle_list[len(obstacle_list) - 1].display())
    guard1 = Guard(guard_x, guard_y, 'N')
    #print(guard1.display())

    guard_path = map_array

    debug_count = 0
    while (guard1.x < map_array.shape[1] and guard1.x >= 0 and guard1.y < map_array.shape[0] and guard1.y >= 0):
        #print(guard1.display())
        guard_path[guard1.y][guard1.x]='X'
        hypothetical_guard=guard1.next_step()
        next_step=Obstacle(hypothetical_guard.x, hypothetical_guard.y)
        collision=False
        for obstacle in obstacle_list:
            #print("Looking for collision at " + obstacle.display())
            if (next_step.x == obstacle.x and next_step.y == obstacle.y):
                collision=True
        if(collision):
            #print("Collision. Guard is turning.")
            guard1.turn()
        else:
            #print("Guard is walking.")
            guard1.walk()
        #mark path on map
        debug_count+=1
    #print("Guard has left the area.")
    #print(guard_path)
    
    step_count=0
    for x in range(map_array.shape[0]):
        for y in range(map_array.shape[1]):
            if (map_array[x][y]=='X'):
                step_count+=1
    print("Guard has walked " + str(step_count) + " steps.")

def findLoops(array):
    print(array)
        #find guard and create object
    guard_x = 0
    guard_y = 0
    obstacle_list = []
    #TODO: check these axes
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            if (array[x][y]=='^'):
                guard_x=y
                guard_y=x
            elif (array[x][y]=='#'):
                obstacle_list.append(Obstacle(y,x))
                #print(obstacle_list[len(obstacle_list) - 1].display())
    original_guard = Guard(guard_x, guard_y, 'N')
    #print(guard1.display())

    infinite_loop_count=0
    print("checking for infinite loops")
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            debug_count = 0
            new_obstacle= Obstacle(y,x)
            #print("Trying new obstacle at: " + new_obstacle.display())
            obstacle_list.append(new_obstacle)

            #print(str(guard_x) + "," + str(guard_y))
            guard1=Guard(guard_x, guard_y, 'N')
            #print(guard1.display())
            while (guard1.x < array.shape[1] and guard1.x >= 0 and guard1.y < array.shape[0] and guard1.y >= 0 and debug_count<10000):
                #print(guard1.display())
                hypothetical_guard=guard1.next_step()
                next_step=Obstacle(hypothetical_guard.x, hypothetical_guard.y)
                collision=False
                for obstacle in obstacle_list:
                    #print("Looking for collision at " + obstacle.display())
                    if (next_step.x == obstacle.x and next_step.y == obstacle.y):
                        collision=True
                if(collision):
                    #print("Collision. Guard is turning.")
                    guard1.turn()
                else:
                    #print("Guard is walking.")
                    guard1.walk()
                #mark path on map
                debug_count+=1
                #if (debug_count%1000==0):
                #    print(str(debug_count) + " steps for obstacle " + new_obstacle.display())
            #print("Guard has left the area.")
            #print(guard_path)
            #print(guard1.display())
            obstacle_list.pop()
            if(debug_count>=10000):
                infinite_loop_count+=1
                print("Infinite loop count: " + str(infinite_loop_count))
    return infinite_loop_count

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

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
    
    def next_step(self):
        hypothetical_guard = Guard(self.x, self.y, self.direction)
        hypothetical_guard.walk()
        return hypothetical_guard
        
    def display(self):
        status = "Guard is at (" + str(self.x) + ", " + str(self.y) + "), facing " + self.direction
        return status
    
if __name__ == "__main__":
    day06part1()