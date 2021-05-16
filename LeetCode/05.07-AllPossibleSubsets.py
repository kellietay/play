def print_subsets(elements, path=[]):
    if not elements:
        print(elements)
        return
    for i,ele in enumerate(elements):
        path.append(ele)
        print(path)
        print_subsets(elements[i+1:],path)
        path.pop()

print_subsets(("a","b"))

#time complexity = O(len(elements))
#space complexity = O(len(elements))