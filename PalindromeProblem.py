# Given a two-dimensional integer array arr of dimensions n x n,
# consisting solely of zeros and ones, identify the row or column (using 0-based indexing) where all elements form a palindrome.
# If multiple palindromes are identified, prioritize the palindromes found in rows over those in columns.
# Within rows or columns, the palindrome with the smaller index takes precedence.
# The result should be represented by the index followed by either 'R' or 'C',
# indicating whether the palindrome was located in a row or column.
# The output should be space-separated. If no palindrome is found, return the string -1.
#
# Examples:
#
# Input:
# arr[][] =  [[1, 0, 0],
#            [0, 1, 0],
#            [1, 1, 0]]
# Output: 1 R
# Explanation: In the first test case, 0-1-0 is a palindrome occurring in a row having index 1.
# Input:
# arr[][] =   [[1, 0],
#            [1, 0]]
# Output: 0 C
# Explanation: 1-1 occurs before 0-0 in the 0th column. And there is no palindrome in the two rows.
# Expected Time Complexity: O(n2)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1<= arr.size <= 50
# 0 <= arr[i][j] <= 1

# <---------- SOLUTION ------------->
arr = [[1, 0, 0],
       [0, 1, 0],
       [1, 1, 0]]


def palindrome_problem(array):
    # because of the zero index, we need to add 1 when calculating midpoint

    n, length = len(array), len(array) - 1
    midpoint = (len(array) - 1) // 2 + 1

    # set the return value to greater than n, so that any row or col smaller become the stand-in return value
    palindrome_row = n + 1
    palindrome_col = n + 1

    # check for palindrome rows and columns, keeping track of the smallest (earliest) seen so far
    for i in range(len(array)):
        col_count, row_count = 0, 0
        for j in range(midpoint):
            if array[i][j] == array[i][length - j]:
                row_count += 1
            if array[j][i] == array[length - j][i]:
                col_count += 1

        if row_count == midpoint:
            palindrome_row = min(palindrome_row, i)
        if col_count == midpoint:
            palindrome_col = min(palindrome_col, i)

    # return row first, then col, if not, return -1
    if palindrome_row < n + 1:
        return str(palindrome_row) + ' R'
    elif palindrome_col < n + 1:
        return str(palindrome_col) + ' C'
    else:
        return -1
# <---------- SOLUTION ------------->

print(palindrome_problem(arr))
