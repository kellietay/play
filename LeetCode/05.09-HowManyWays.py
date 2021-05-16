def ways_to_buy(steps:list, target:int, result=0):
    if target == 0:
        return 1
    elif target < 0:
        return 0
    
    for i,step in enumerate(steps):
        result += ways_to_buy(steps[i:],target-step)
    
    return result

print(ways_to_buy([],3)) #0
print(ways_to_buy([1],3)) #1
print(ways_to_buy([3,3],6)) #3
print(ways_to_buy([10,15,50],60)) #4
