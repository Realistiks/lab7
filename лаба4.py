students = [
    ("Иван", 20, 4.5),
    ("Мария", 22, 4.8),
    ("Пётр", 21, 4.2),
    ("Анна", 19, 4.9),
]

print(f'{"Имя":<10}{"Возраст":>10}{"Балл":>10}')
print("-" * 30)
for name, age, score in students:
    print(f"{name:<10}{age:>10}{score:>10.2f}")

oldest = students[0]
best = students[0]
total_age = 0

for s in students:
    if s[1] > oldest[1]:
        oldest = s
    if s[2] > best[2]:
        best = s
    total_age += s[1]

print("-" * 30)
age = oldest[1]
if age % 10 == 1 and age % 100 != 11:
    word = "год"
elif 2 <= age % 10 <= 4 and age % 100 not in (12, 13, 14):
    word = "года"
else:
    word = "лет"
print(f"Самый старший: {oldest[0]}, {age} {word}")
print(f"Самый высокий балл: {best[0]}, {best[2]:.2f}")
print(f"Средний возраст: {total_age / len(students):.1f}")
