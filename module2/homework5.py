#Тема "Функции в Python. Функция с параметром". Задача "Матрица воплоти"

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

print(f"Матрица = {get_matrix(4,6,1)}")
print(f"Вторая матрица = {get_matrix(5,2,3)}")
print(f"Третья матрица = {get_matrix(1,2,42)}")