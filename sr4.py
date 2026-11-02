print("Размер матриц N")
n = int(input())

print("Матрица A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

print("Матрица B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])

add = []
sub = []

for i in range(n):
    row_add = []
    row_sub = []
    for j in range(n):
        row_add.append(a[i][j] + b[i][j])
        row_sub.append(a[i][j] - b[i][j])
    add.append(row_add)
    sub.append(row_sub)

mult = []
for i in range(n):
    row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total += a[i][k] * b[k][j]
        row.append(total)
    mult.append(row)

print()
print("A + B")
for row in add:
    print(" ".join(f"{x:>4}" for x in row))

print()
print("A - B")
for row in sub:
    print(" ".join(f"{x:>4}" for x in row))

print()
print("A * B")
for row in mult:
    print(" ".join(f"{x:>5}" for x in row))
