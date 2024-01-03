# s = "aaabbccc" 

# charArray = [] # 최종 문자열 저장 배열
# cnt = 1
# for i in range(len(s)):
#     # print(f's[i]:{s[i]} | s[i + 1]:{s[i + 1]}') 
#     if s[i] == s[i + 1]:
#         cnt += 1
#         print(f'cnt:{cnt}')
#     elif s[i] != s[i + 1]:
#         charArray.append(s[i] + str(cnt))
#         print(f'charArray: {charArray}')
#         cnt = 1
#     elif s[i + 1] == None:
#         charArray.append(s[i] + str(cnt))
#         print(f'charArray: {charArray}')


# print(charArray)

# num  = [1, 2, 3]
# for i in range(len(num)):
#     if num[i + 1] != None:
#         print(num[i])

matrix = [[5, 4, 0, 2], [0, 2, 3, 4], [4, 1, 2, 3], [7, 6, 5, 0]]

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

# 출력
for i in range(row_size):
    for j in range(col_size):
        print(matrix[i][j], end=" ")
    print()

print(matrix)

# print(changed_rows)
# print(changed_cols)


