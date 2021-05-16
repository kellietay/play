def is_palindrome(input:int):
    current = input
    input_list = []
    while current != 0:
        input_list.append(current % 10)
        current = current // 10

    if len(input_list) <= 1:
        return True
    for i in range(0, int(len(input_list)/2)):
        left = input_list[i]
        right = input_list[-i-1]
        if left != right:
            return False
    return True

print(is_palindrome(12345)) #       false            
print(is_palindrome(12321)) #       true            
print(is_palindrome(11111)) #       true            
print(is_palindrome(1221))  #       true            
print(is_palindrome(6))     #       true            
print(is_palindrome(0))     #       true

#time O(n), space O(n): n=len(input)