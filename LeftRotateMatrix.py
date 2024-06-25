# You are given an integer k and matrix mat.
# Rotate the elements of the given matrix to the left k times and return the resulting matrix.

k = 1
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def left_rotate_matrix(matrix, k):
    # let the dimensions of the matrix be n x m
    n, m = len(matrix), len(matrix[0])

    # if k is bigger than the number of rows, reduce it to the modulo, to avoiding cycling through the matrix
    if k > m:
        k = k % m

    for row in matrix:
        temp = row[0:k]

        for i in range(k, m):
            row[i - k] = row[i]
        row[m - k:] = temp
    return matrix


print(left_rotate_matrix(mat, k))