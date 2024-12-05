def day05part1():
    print("day 5, part 1")
    # f = open("advent-2024-05-input.txt")
    input_file = open("advent-2024-05-input-small.txt")
    rules_file = open("advent-2024-05-rules-small.txt")
    rules_list=[]
    for x in rules_file:
        rules_list.append(x)
    print(rules_list)

    input_list=[]
    for x in input_file:
        input_list.append(x)
    print(input_list)
        

    middle_average=0
    input_file.close
    rules_file.close
    print("Middle average: " + str(middle_average))

def day05part2():
    print("day 5, part 2")
    # f = open("advent-2024-05-input.txt")
    input_file = open("advent-2024-05-input-small.txt")
    rules_file = open("advent-2024-05-rules-small.txt")
    rules_list=[]
    for x in rules_file:
        rules_list.append(x)

    middle_average=0
    input_file.close
    rules_file.close
    print("Middle average: " + str(middle_average))

if __name__ == "__main__":
    day05part1()
    day05part2()