"""
Corner Cases:
- if the first char is a ?
- will it only have 1,0 and ? : yes
"""
            

def perm(s, i=0):
    if i == len(s):
        print(s)
        return        

    if i == 0 and s[i] == "?":
        perm("1" + s[1:], i+1)
        perm("0" + s[1:], i+1)
    
    elif s[i] == "?":
        perm(s[:i] + "1" + s[i+1:], i+1)
        perm(s[:i] + "0" + s[i+1:], i+1)
    
    else:
        perm(s,i+1)

a = "?01?"
b = "????"
c = "0??0"

print("a")
perm(a)
print("b")
perm(b)
print("c")
perm(c)