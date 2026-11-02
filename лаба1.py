import random

print("Сколько чисел?")
n = int(input())

if n < 1:
    print("N должно быть больше 0")
else:
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 20))

    print("Список:", " ".join(str(x) for x in numbers))
    print("Сумма:", sum(numbers))
    print(f"Среднее: {sum(numbers) / n:.2f}")
    print("Минимум:", min(numbers))
    print("Максимум:", max(numbers))

    ordered = sorted(numbers)
    print("Отсортировано:", " ".join(str(x) for x in ordered))

    unique = []
    for x in numbers:
        if x not in unique:
            unique.append(x)
    print("Без дубликатов:", " ".join(str(x) for x in unique))
