# "Генераторные сборки"
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(x[0]) - len(x[1]) for x in list(zip(first, second)) if len(x[0]) != len(x[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))

# Пример выполнения кода:
print(list(first_result))
print(list(second_result))

# Вывод в консоль:
# [1, 2]
# [False, False, True]
