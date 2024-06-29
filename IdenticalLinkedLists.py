# Given the two singly Linked Lists respectively.
# The task is to check whether two linked lists are identical or not.
# Two Linked Lists are identical when they have the same data and with the same arrangement too.
# If both Linked Lists are identical then return true otherwise return false.
#
# Examples:
#
# Input:
# LinkedList1: 1->2->3->4->5->6
# LinkedList2: 99->59->42->20
# Output: false
# Explanation:

# Input:
# LinkedList1: 1->2->3->4->5
# LinkedList2: 1->2->3->4->5
# Output: true
# Explanation:
#
# As# shown in figure# both# are# identical.
# Expected Time
# Complexity: O(n)
# Expected# Auxiliary Space: O(1)
#
# Constraints: 1 <= length of  lists <= 103

# <--------------- SOLUTION -------------------->

# define the node of a linked list
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# create a linked list from an array
def create_linkedlist(arr):
    prev = Node()

    for i in reversed(range(len(arr))):
        temp = Node(val=arr[i], next=prev)
        prev = temp

    return prev


arr1 = [1, 2, 3, 4, 2]
arr2 = [1, 2, 3, 4, 2, 4]
arr3 = [1, 3, 4, 5, 9]

l1 = create_linkedlist(arr1)
l2 = create_linkedlist(arr2)
l3 = create_linkedlist(arr3)


# check if two linked lists are identical
def identical_linked_list(node1, node2):
    while node1.next or node2.next:  # to ensure that they are of the same length
        if node1.val != node2.val:
            return False
        else:
            node1 = node1.next
            node2 = node2.next
    return True


print(identical_linked_list(l1, l3))
# <--------------- SOLUTION -------------------->
