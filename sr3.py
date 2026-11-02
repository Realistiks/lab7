print("Введите отсортированные числа через пробел")
arr = [int(x) for x in input().split()]

print("Какое число искать?")
key = int(input())

left = 0
right = len(arr) - 1
index = -1
steps = 0

while left <= right:
    steps += 1
    mid = (left + right) // 2
    if arr[mid] == key:
        index = mid
        break
    elif arr[mid] < key:
        left = mid + 1
    else:
        right = mid - 1

if index != -1:
    print(f"Число {key} найдено на позиции {index}, сравнений: {steps}")
else:
    print(f"Числа {key} в списке нет, сравнений: {steps}")
