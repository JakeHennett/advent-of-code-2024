def main_day03():
    print("day 3")
    f = open("advent-2024-03-input.txt")
    #f = open("advent-2024-03-input-small.txt")
    mul_list=[]
    for x in f:
        #print("x: " + x)
        remaining_string=x
        next_index=remaining_string.find("mul(")
        #print("the first occurence of mul begins at: " + str(next_index))
        new_substring=remaining_string
        while next_index > -1:
        #if next_index > -1:
            new_substring=new_substring[next_index:]
            #print("this should begin with mul: " + new_substring)
            mul_substring_length=new_substring.find(")")
            #print("chars until close paren: " + str(mul_substring_length))
            #TODO: check that 12 is enough for 2 nums of 3 digits each.
            if (mul_substring_length > -1 and mul_substring_length < 12):
                #Found a valid mul
                mul_sub = new_substring[0:mul_substring_length+1]
                #print("individual mul operation: " + mul_sub)
                mul_list.append(mul_sub)
                new_substring=new_substring[mul_substring_length:]
            elif (mul_substring_length > -1):
                #Found a mul but length is too long. Advance and try again
                new_substring=new_substring[1:]
            else:
                print("No more mul operations found")
            #print(new_substring)
            next_index=new_substring.find("mul(")
            #print(next_index)
    
    mul_sum=0
    for x in mul_list:
        #print("mul_list item: " + x)
        numbers_only=x[4:len(x)-1]
        num_list=numbers_only.split(",")
        #print(numbers_only)
        #print(num_list)
        try:
            product=int(num_list[0])*int(num_list[1])
        except:
            product=0
        #print(product)
        mul_sum+=product
    print("Sum of all mul operations: " + str(mul_sum))

    #close file
    f.close()

def main_day03part2():
    print("day 3, part 2")
    f = open("advent-2024-03-input.txt")
    #f = open("advent-2024-03-input-small.txt")
    mul_list=[]
    for x in f:
        #print("x: " + x)
        remaining_string=x
        next_index=remaining_string.find("mul(")
        #print("the first occurence of mul begins at: " + str(next_index))
        new_substring=remaining_string
        while next_index > -1:
        #if next_index > -1:
            new_substring=new_substring[next_index:]
            #print("this should begin with mul: " + new_substring)
            mul_substring_length=new_substring.find(")")
            #print("chars until close paren: " + str(mul_substring_length))
            #TODO: check that 12 is enough for 2 nums of 3 digits each.
            if (mul_substring_length > -1 and mul_substring_length < 12):
                #Found a valid mul
                mul_sub = new_substring[0:mul_substring_length+1]
                #print("individual mul operation: " + mul_sub)
                mul_list.append(mul_sub)
                new_substring=new_substring[mul_substring_length:]
            elif (mul_substring_length > -1):
                #Found a mul but length is too long. Advance and try again
                new_substring=new_substring[1:]
            else:
                print("No more mul operations found")
            #print(new_substring)
            next_index=new_substring.find("mul(")
            #print(next_index)
    
    mul_sum=0
    for x in mul_list:
        #print("mul_list item: " + x)
        numbers_only=x[4:len(x)-1]
        num_list=numbers_only.split(",")
        #print(numbers_only)
        #print(num_list)
        try:
            product=int(num_list[0])*int(num_list[1])
        except:
            product=0
        #print(product)
        mul_sum+=product
    print("Sum of all mul operations: " + str(mul_sum))

    #close file
    f.close()