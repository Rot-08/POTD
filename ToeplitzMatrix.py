# A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant,
# i.e., all elements in a diagonal are the same.
# Given a rectangular matrix mat, your task is to complete the function isToeplitz which returns true if the matrix is Toeplitz
# otherwise, it returns false.
#
# Examples:
#
# Input:
# mat = [[6, 7, 8],
#        [4, 6, 7],
#        [1, 4, 6]]
# Output: true
# Explanation: The test case represents a 3x3 matrix
#  6 7 8
#  4 6 7
#  1 4 6
# Output will be true, as values in all downward diagonals from left to right contain the same elements.
# Input:
# mat = [[1,2,3],
#        [4,5,6]]
# Output: false
# Explanation: Matrix of order 2x3 will be 1 2 3 4 5 6 Output: false as values in all diagonals are not the same.

# <------------------ SOLUTION -------------------->


mat = [[1,2,3],
        [4,5,6]]
# Let the size of the matrix be n x m (rows x columns)

def isToeplitz(matrix):
    n = len(matrix)
    if n != 1:  # to check that it is not a row vector
        m = len(matrix[0])
        if m != 1:  # to check that it is not a column vector
            for i in range(n - 1):
                for j in range(m - 1):
                    if matrix[i][j] != matrix[i + 1][j + 1]:
                        return False
                    else:
                        continue
            return True
        else:
            return False
    else:
        return False

# <------------------ SOLUTION -------------------->

print(isToeplitz(mat))