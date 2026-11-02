print("Строк и столбцов через пробел")
size = input().split()
rows = int(size[0])
cols = int(size[1])

print("Введите строки матрицы")
matrix = []
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

print()
print("Исходная матрица:")
for row in matrix:
    print(" ".join(f"{x:>4}" for x in row))

transposed = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print()
print("Транспонированная матрица:")
for row in transposed:
    print(" ".join(f"{x:>4}" for x in row))
