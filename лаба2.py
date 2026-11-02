print("Введите числа через пробел")
arr = [int(x) for x in input().split()]

seen = []
duplicates = []

for x in arr:
    if x not in seen:
        seen.append(x)
    elif x not in duplicates:
        duplicates.append(x)

if len(duplicates) == 0:
    print("Дубликатов нет")
else:
    print("Дубликаты:")
    for d in duplicates:
        count = arr.count(d)
        if count % 10 == 1 and count % 100 != 11:
            word = "раз"
        elif 2 <= count % 10 <= 4 and count % 100 not in (12, 13, 14):
            word = "раза"
        else:
            word = "раз"
        print(f"  {d} — встречается {count} {word}")
