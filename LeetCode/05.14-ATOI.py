def ATOI(s1):
    num_dict = {"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
    num = 0
    if s1[0] == "-":
        start_i = 1
    else:
        start_i = 0
    
    for i in range(start_i,len(s1)):
        num *= 10
        if num_dict.get(s1[i]):
            num += num_dict[s1[i]]
        else:
            return None
        
    if start_i == 1:
        num *= (-1)

    return num

s1="123"
s2="-123"
s3="12233"

print(ATOI(s1))
print(ATOI(s2))
print(ATOI(s3))



