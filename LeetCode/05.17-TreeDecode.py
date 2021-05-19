class Node():
    def __init__(self,value,child=None):
        self.value = value
        self.child = child

    def __repr__(self):
        return self.value

root = Node("",[Node("a"),Node("*",[Node("b"),Node("c"),Node("d")])])
print(root.child)

def build_tree(root, path="", decode_dict={}):
    if not root.child:
        return
    count = -1
    for n in root.child:
        count += 1
        if n.value != "*":
            decode_dict[path+str(count)] = n.value
        build_tree(n,path+str(count),decode_dict)
    return decode_dict

def decode(s,root):
    decode_dict = build_tree(root)
    current = ""
    result = ""
    for char in s:
        current = current + char
        if decode_dict.get(current):
            result += decode_dict[current]
            current = ""
    return result

print(decode("0101011",root)) #abbc
print(decode("10101111",root)) #bbcc
print(decode("001010101111",root)) #aabbbcc
print(decode("0101112",root)) #abcd

