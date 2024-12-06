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
    #print(rules_list)

    input_list=[]
    for x in input_file:
        input_list.append(x)
    #print(input_list)
    
    sorted_list=input_list
    total_middle_sum=0
    correct_middle_sum=0
    incorrect_middle_sum=0
    for page in sorted_list:
        #print("Checking page containing rules: " + page)
        page = page.split(',')
        page[len(page)-1]=page[len(page)-1][0:2] #remove newline character from last element
        page_sorted=False
        loop_count=0
        while (not page_sorted):
            #print("loop count = " + str(loop_count))
            #TODO: Change this check to a valid check once we know what to look for
            if (page_sorted):
                print("Page is sorted!")
                page_sorted=True
            else:
                #print("We must sort the page.")
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
                        #print("Reordering items at " + str(first_rule_index) + " and " + str(second_rule_index) + " because " + page[first_rule_index] + " must come before " + page[second_rule_index])
                        #print(page)
                        page.insert(first_rule_index, page.pop(second_rule_index))
                        #print(page)

                    #print("Rule items found at indices: " + str(first_rule_index) + " and " + str(second_rule_index))
            loop_count+=1
        #print("While loop is finished. Page must be sorted now.")
        #print(page)
        middle_element = int(page[math.floor(len(page)/2)])
        if(loop_count == 1): #correct ordering on the first pass
            correct_middle_sum+=middle_element
        else:
            incorrect_middle_sum+=middle_element
        #print("page length is " + str(len(page)) + " so middle index is " + str(math.floor(len(page)/2)) + " which has a value of...")
        #print(middle_element)
        total_middle_sum+=middle_element


    input_file.close
    rules_file.close
    print("Total middle sum: " + str(total_middle_sum))
    print("Correct middle sum (part 1 solution): " + str(correct_middle_sum))
    print("Incorrect middle sum (part 2 solution): " + str(incorrect_middle_sum))
    #10058 is too high
    #9362 too high
    #5087 is just right

if __name__ == "__main__":
    day05part1()