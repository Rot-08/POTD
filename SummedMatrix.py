# A matrix is constructed of size n*n and given an integer ‘q’.
# The value at every cell of the matrix is given as, M(i,j) = i+j,
# where ‘M(i,j)' is the value of a cell, ‘i’ is the row number, and ‘j’ is the column number.
# Return the number of cells having value ‘q’.

# #Note: Assume, the array is in 1-based indexing.
# Input: n = 4, q = 7
# Output: 2
# Explanation: Matrix becomes
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 5 6 7 8
# The count of 7 is 2.

try:
    n = int(input("n: "))
    q = int(input("q: "))

    count = 0

# if n is greater than q, that means in the first column of the matrix, q is at position (n-q)
# it will continue showing up until row (n-1) - (n-q), hence it will appear q-1 times
    if n-q > 0:
        count = q-1

# if n is equal q, that means in the first column of the matrix q is at position (n)
# it will continue showing up until row: n-1
    elif n-q == 0:
        count = n-1

# if n is less than q, that means q will first appear at row (q - n)
# it will continue showing up until the last row: (n+1), hence it will show up (n+1) - (q-n) times or 2n + 1 - q.
    elif n-q < 0:
        count = 1 + 2*n - q

    print(count)

# in case the input is invalid
except Exception as e:
    print(e)





