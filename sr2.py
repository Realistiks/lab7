def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)


print("Введите числа через пробел")
arr = [int(x) for x in input().split()]

print("Отсортировано:", " ".join(str(x) for x in quick_sort(arr)))
