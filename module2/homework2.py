#Тема "Опреатор if" (с добавлением циклов)

first, second, third = [int(input()) for x in range(3)]

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)