from typing import List

def zero_matrix(matrix: List[List[int]], row: int, col: int) -> List[List[int]]:
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire
    row and column are set to 0.
    """
    col_size = len(matrix[0])
    row_size = len(matrix)

    # col 위치의 element들을 0으로 바꾸기
    for i in range(row_size):
        matrix[i][col] = 0
        
    # row 위치의 element들을 0으로 바꾸기
    for i in range(col_size):
        matrix[row][i] = 0
    return matrix

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    result1 = [[1, 0, 3], [0, 0, 0], [1, 0, 3]]
    # col_size = 3, row_size = 3

    testcase2 = [[5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3, 3]]
    result2 = [[5, 0, 5, 5], [0, 0, 0, 0], [3, 0, 3, 3]]
    # col_size = 4, row_size = 3

    assert zero_matrix(testcase1, 1, 1) == result1
    assert zero_matrix(testcase2, 1, 1) == result2