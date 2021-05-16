def closest_pair(array:list):
    if len(array) < 2:
        return array(0), array(0)
    array.sort()
    smallest = abs(array[0] - array[1])
    smallest_list = [array[0], array[1]]

    for i in range(1,len(array)-1):
        current = abs(array[i]-array[i+1])
        if current < smallest:
            smallest = current
            smallest_list = [array[i],array[i+1]]

    return smallest_list[0], smallest_list[1]

#Time = O(nlog(n)), Space = O(n) where n = len(array)


print(closest_pair([32,71,12,45,26,80,34,43])) #returns 32,34