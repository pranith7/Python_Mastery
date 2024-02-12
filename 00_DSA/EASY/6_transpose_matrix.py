""" 
Problem Statement:

    Given a 2D integer array matrix, return the transpose of matrix.

    The transpose of a matrix is the matrix flipped over its main diagonal, 
    switching the matrix's row and column indices.

    Example 1:

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

    Example 2:

    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]

"""

from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """
    Approach 1:- | Time complexity:- O(R*C) | Space complexity:- O(R*C)

    we are using a simple approach to return transpose of matrix
    1. We are addiing a check at initial stage whether matrix is empty or not.
    2. We are declaring an transpose matrix with zero's for the same rows and columns.
    3. Then we iterate through the matrix and overwrite the positions with [j][i] values
    4. Returning the transpose matrix.

    Approach 2:- Time complexity:- O(R*C) | Space complexity:- O(R*C)

    We are performing same technique as previous one but we are updating the values in
    transpose in efficient manner.
    1. We are addiing a check at initial stage whether matrix is empty or not.
    2. We are iterating over the matrix and adding all the values in an temp list
       which declared whie iterating to a new row and appending it' value to transpose list.
    """
    #  code for Approach-1
    # if not matrix or not matrix[0]:
    #     return []

    # rows, colums = len(matrix) , len(matrix[0])

    # transpose = [[0 for _  in range(rows)] for _ in range(colums)]

    # for i in range(rows):
    #     for j in range(colums):
    #         transpose[j][i] = matrix[i][j]

    # return transpose

    # code for Approach-2
    if not matrix or not matrix[0]:
        return []

    rows, colums = len(matrix), len(matrix[0])
    transpose = []
    for i in range(rows):
        temp = []
        for j in range(colums):
            temp.append(matrix[j][i])
        transpose.append(temp)
    return transpose


# Example input matrix
input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpose the matrix
transposed_matrix = transpose(input_matrix)

# Print the original and transposed matrices
print("Original Matrix:")
for row in input_matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
