#Дополнительное практическое задание по модулю: "Основные операторы"
a = int(input("Введите число"  ))

lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == a:
            result.append(lst[i])
            result.append(lst[j])

for str in result:
    print(str, end="")