# Given a doubly Linked list and a position. 
# The task is to delete a node from a given position 
# (position starts from 1) in a doubly linked list and return the head of the doubly Linked list.

# Examples:

# Input: LinkedList = 1 <--> 3 <--> 4, x = 3
# Output: 1 3  
# Explanation: 
# After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.
 
# Input: LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
# Output: 5 2 9
# Explanation:

# Expected Time Complexity: O(n)
# Expected Auxilliary Space: O(1)

# Constraints:
# 2 <= size of the linked list(n) <= 105
# 1 <= x <= n
# 1 <= node.data <= 109

# <----------- SOLUTION ------------>

# first create a node of the linked list
class Node:
    def __init__(self, prev = None, next = None, val = 0):
        self.prev = prev
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

# create a doubly-linked list from an array
def create_linked_list(arr):
    for i in range(len(arr)):
        arr[i] = Node(val = arr[i])
        arr[i].prev = arr[i-1]

    arr[0].prev = Node()
    arr[-1].next = Node()

    for i in range(len(arr)-1):
        arr[i].next = arr[i+1]

    return arr[0]
    
# display the linked list
def display_linked_list(first_node):
    while(first_node.next):
        print(first_node, end=' ')
        first_node = first_node.next

# let k = 3
k = 3
def remove_element(node, k):
    if k == 1:
        node = node.next
        return node
    else:
        count = 1
        while(count != k ):
            node = node.next
            count += 1
        node.prev.next = node.next
        node.next.prev = node.prev
        
        while(count > 1):
            node = node.prev
            count -= 1
        return node
        



node = create_linked_list([_ for _ in range(1, 21)])

node = remove_element(node, 1)
display_linked_list(node)

