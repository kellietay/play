"""
Given two positive integers as two singly linked lists of digits
implement a function to add the two numbers and procude the sum also as singly linked list of digits

1>2>3 + 4>5>6 = 5>7>9
1>5 + 1>7>7 = 1>7>9
9>9>9 + 1 = 1>0>0>0

Corner Cases:
- one list is empty: return non empty list
- both empty: return empty Node(0)
- different number of digits: count the length
- summation > 10: need a carry

"""
class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, start=None):
        self.start = start
        
        current = start
        count = 0
        while current.next:
            count += 1
            current = current.next
        count += 1
        
        self.length = count
        self.end = current
    
    @classmethod
    def sumLists(cls, L1, L2):
        if not L1.start and not L2.start:
            return Node(0)
        if not L1.start:
            return L2.start
        if not L2.start:
            return L1.start
        
        def helper(L1, L2, len_L1, len_L2):
            if len_L1 == 1 and len_L2 == 1:
                sum = (L1.value + L2.value)
                return(Node(sum % 10), sum // 10)

            elif len_L1 == len_L2:
                result_node,carry = helper(L1.next, L2.next, len_L1-1, len_L2-1)
                sum = L1.value + L2.value + carry

            elif len_L1 > len_L2:
                result_node,carry = helper(L1.next, L2, len_L1-1, len_L2)
                sum = L1.value + carry

            elif len_L2 > len_L1:
                result_node,carry  = helper(L1, L2.next, len_L1, len_L2-1)
                sum = L2.value + carry 

            L3 = Node(sum % 10, result_node)
            return(L3, sum // 10)
            
        result_node, carry = helper(L1.start,L2.start,L1.length, L2.length)
        if carry != 0:
            return Node(carry, result_node)
        else:
            return result_node

obj_L1 = LinkedList(Node(1, Node(5)))
obj_L2 = LinkedList(Node(1, Node(7, Node(9))))
current = LinkedList.sumLists(obj_L1, obj_L2)

while current:
    print(current.value)
    current = current.next

obj_L3 = LinkedList(Node(1))
obj_L4 = LinkedList(Node(9, Node(9, Node(9))))
current1 = LinkedList.sumLists(obj_L3, obj_L4)

while current1:
    print(current1.value)
    current1 = current1.next
