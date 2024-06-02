#Тема "Индексация строк"

example = "Дроконорожденный"

# 1. Выведите на экран первый символ строки

print(f"Первый символ этой строки = {example[0]}")

# 2. Выведите на экран последний символ этой строки

print(f"Последний символ этой строки = {example[-1]}")

# 3. Выведите на экран вторую половину этой строки

print(f"Вторая половина этой строки = {example[len(example)//2:]}")

# 4. Выведите на экран это слово наоборот

print(f"Слово наоборот = {''.join(reversed(example))}")

# 5. Выведите на экран каждый второй символ этой строки.

print(f"Каждый второй символ этой строки = {example[1:len(example):2]}")