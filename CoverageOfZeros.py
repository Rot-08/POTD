# Given a binary matrix contains 0s and 1s only we need to find the sum of coverage of all zeros of the matrix where
# coverage for a particular 0 is defined as a total number of ones around a zero in left, right, up and bottom
# directions.
#
# Examples:
#
# Input:
# matrix = [[0, 1, 0],
#           [0, 1, 1],
#           [0, 0, 0]]
# Output: 6
# Explanation: There are a total of 6 coverage are there
#
# Input:
# matrix = [[0, 1]]
# Output: 1
# Explanation: There are only 1 coverage.

# <--------------- Solution -------------------->

# Since the matrix is made up of just 0's and 1's, the difference between the (sum of the elements in the matrix) and
# (number of elements in the matrix) is (the number of Zeros)

mat = [[0, 1]]


def coverage_of_zeros(matrix):
    sum_of_elements = 0

    for row in matrix:
        sum_of_elements += sum(row)

    num_of_elements = len(matrix) * len(matrix[0])

    return num_of_elements - sum_of_elements

print(coverage_of_zeros(mat))
