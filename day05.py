import math

def day05part1():
    print("day 5, part 1")
    # f = open("advent-2024-05-input.txt")
    #input_file = open("advent-2024-05-input-small.txt")
    #rules_file = open("advent-2024-05-rules-small.txt")
    input_file = open("advent-2024-05-input.txt")
    rules_file = open("advent-2024-05-rules.txt")
    rules_list=[]
    for x in rules_file:
        rules_list.append(x)
    print(rules_list)

    input_list=[]
    for x in input_file:
        input_list.append(x)
    print(input_list)
    
    sorted_list=input_list
    middle_average=0
    for page in sorted_list:
        print("Checking page containing rules: " + page)
        page = page.split(',')
        page[len(page)-1]=page[len(page)-1][0:2] #remove newline character from last element
        page_sorted=False
        while (not page_sorted):
            #TODO: Change this check to a valid check once we know what to look for
            if (page_sorted):
                print("Page is sorted!")
                page_sorted=True
            else:
                print("We must sort the page.")
                page_sorted=True #assuming page is sorted properly unless we find otherwise
                for rule in rules_list:
                    #break rule into two numbers
                    rule = rule.split("|")
                    rule[1] = rule[1][0:2]
                    #print(rule)
                    #check if both rules are in the current page
                    try:
                        first_rule_index=page.index(rule[0])
                        second_rule_index=page.index(rule[1])
                    except:
                        first_rule_index=-1
                        second_rule_index=-1
                        #print("Page does not contain both rule items")
                    
                    #check if indices are in the correct order
                    if (first_rule_index > second_rule_index):
                        page_sorted=False #at least one rule was not followed
                        print("Reordering items at " + str(first_rule_index) + " and " + str(second_rule_index) + " because " + page[first_rule_index] + " must come before " + page[second_rule_index])
                        #l.insert(newindex, l.pop(oldindex))
                        print(page)
                        page.insert(first_rule_index, page.pop(second_rule_index))
                        print(page)

                    #print("Rule items found at indices: " + str(first_rule_index) + " and " + str(second_rule_index))
            #Check if page already matches rules
            #iterate over rules list once and edit as necessary
            #page_sorted=True #TODO: remove this hard coded assertion once logic works
        print("While loop is finished. Page must be sorted now.")
        print(page)
        middle_element = int(page[math.floor(len(page)/2)])
        print(middle_element)
        middle_average+=middle_element


    input_file.close
    rules_file.close
    print("Middle average: " + str(middle_average))
    #10058 is too high

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