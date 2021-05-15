"""
https://leetcode.com/problems/valid-parentheses/

Sample Input: [1,{3},{4,(2*(4*2)/3)}]
Return: True

"""

def validParentheses(equation:str):
    close_par = {"}":"{", "]":"[", ")":"("}
    open_par = ("{", "[", "(")
    stack = []

    for char in equation:
        if char in open_par:
            stack.append(char)
        elif char in close_par:
            last = stack.pop()
            if close_par[char] != last:
                return False
    return True

A = validParentheses("[1,{3},{4,(2*(4*2)/3)}]")
print(A) #True

B = validParentheses("[1,{3},{4,(2*(4*2/3)}]")
print(B) #False