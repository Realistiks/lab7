stack = []

print("Стек на списке")
print("1 - добавить (push)")
print("2 - удалить (pop)")
print("3 - вершина стека")
print("4 - показать стек")
print("0 - выход")

while True:
    command = input("Команда: ")

    if command == "1":
        value = input("Значение: ")
        stack.append(value)
        print("Добавлено:", value)
    elif command == "2":
        if len(stack) == 0:
            print("Стек пуст")
        else:
            print("Удалено:", stack.pop())
    elif command == "3":
        if len(stack) == 0:
            print("Стек пуст")
        else:
            print("Вершина:", stack[-1])
    elif command == "4":
        if len(stack) == 0:
            print("Стек пуст")
        else:
            print("Стек:", " ".join(stack))
    elif command == "0":
        print("Выход")
        break
    else:
        print("Нет такой команды")
