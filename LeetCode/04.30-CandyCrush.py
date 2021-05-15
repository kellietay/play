#define a node of a single linked list
#input = string
#output = string

"""
Thought Process:
need a method to store the nodes. Can be done using a stack. use list[char, count] to keep count

Edge Cases:
- initialize the stack or if there is no items in the stack
- if the candies have a length greater than 3 e.g. AABBBAAC -> C and not AC
- last candy in the stack needs to be processed

For each current_candy:
    if stack is blank:
        then add [char, count]
    else if stack is not blank:
        if current_candy == candy_stack[-1][0]:
            increase count of candy_stack[-1][1] by 1
        else:
            if count of top most item in candy_stack > 3:
                pop from stack
                if current_candy == last item i stack: #this might give error if the stack is blank
                    increase count
                else:
                    append current_candy, count = 1

if candy_stack and count of last item > 3:
    pop

join the items in the stack back into a string

"""

def CandyCrush(candies):
    candy_stack = []
    for candy in candies:
        if not candy_stack:
            candy_stack.append([candy,1])
        else:
            if candy == candy_stack[-1][0]: 
                candy_stack[-1][1] += 1
            else:
                if candy_stack[-1][1] >= 3:
                    candy_stack.pop()
                if candy_stack and candy == candy_stack[-1][0]: 
                    candy_stack[-1][1] += 1
                else:
                    candy_stack.append([candy,1])
    if candy_stack and candy_stack[-1][1] >= 3:
        candy_stack.pop()
    return "".join(candy[0] * candy[1] for candy in candy_stack)



A = CandyCrush("AABBBAAC")
print(A) #returns C

B = CandyCrush("ZCCAABBBAACC")
print(B) #returns Z