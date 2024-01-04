from typing import List

def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire
    row and column are set to 0.
    """
    col_size = len(matrix[0])
    row_size = len(matrix)

    changed_rows = []
    changed_cols = []

    # 값이 0인 행과 열 저장
    for i in range(row_size):
        for j in range(col_size):
            if matrix[i][j] == 0:
                changed_rows.append(i)
                changed_cols.append(j)

    # 바꾸기
    # 행
    for i in changed_rows:
        for j in range(col_size):
            matrix[i][j] = 0
    # 열
    for i in changed_cols:
        for j in range(row_size):
            matrix[j][i] = 0

    return matrix

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = [[5, 4, 0], [1, 1, 1], [2, 1, 3], [0, 9, 7]]
    result1 = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]
    # col_size = 3, row_size = 4

    assert zero_matrix(testcase1) == result1