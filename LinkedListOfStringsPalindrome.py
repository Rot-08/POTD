# Given a linked list with string data, 
# check whether the combined string formed is palindrome.
#  If the combined string is palindrome then return true otherwise return false.

# Example:

# Input:

# Output : true
# Explanation: As string "abcddcba" is palindrome the function should return true.
# Input:

# Output : false
# Explanation: As string "abcdba" is not palindrome the function should return false.
# Expected Time Complexity:  O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= Node.data.length<= 103
# 1<=list.length<=103

# <------------- SOLUTION ---------------->

class Node:
    def __init__(self, next = None, val = ''):
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

# create a doubly-linked list from an array
def create_linked_list(string):
    arr = [string[i] for i in range(len(string))]
    for i in range(len(arr)):
        arr[i] = Node(val = arr[i])

    for i in range(len(arr)-1):
        arr[i].next = arr[i+1]
    arr[-1].next = None

    return arr[0]
    
# display the linked list
def display_linked_list(first_node):
    while(first_node):
        print(first_node, end=' ')
        first_node = first_node.next
    print()
    


# change them back to an array/string
def linked_list_to_string(node):
    string = ''
    while(node):
        string += node.val
        node = node.next
    return string


# check if the array/string is a palindrome
def is_Palindrome(string):
    midpoint = len(string)//2
    for i in range(midpoint):
        if string[i] != string[len(string) - (i+1)]:
            return False
    return True

        

# <------------------------------->
node = create_linked_list("abcdba")
string = linked_list_to_string(node)
print(is_Palindrome(string))
# <------------------------------->

# <------------- SOLUTION ---------------->