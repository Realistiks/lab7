print("Первый список")
a = [int(x) for x in input().split()]
print("Второй список")
b = [int(x) for x in input().split()]

union = []
for x in a + b:
    if x not in union:
        union.append(x)

intersection = []
for x in a:
    if x in b and x not in intersection:
        intersection.append(x)

difference = []
for x in a:
    if x not in b and x not in difference:
        difference.append(x)

print()
print(f'{"Первый список:":<14}', " ".join(str(x) for x in a))
print(f'{"Второй список:":<14}', " ".join(str(x) for x in b))
print(f'{"Объединение:":<14}', " ".join(str(x) for x in union))
print(f'{"Пересечение:":<14}', " ".join(str(x) for x in intersection))
print(f'{"Разность:":<14}', " ".join(str(x) for x in difference))
