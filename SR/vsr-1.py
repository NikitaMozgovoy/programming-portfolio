from time import perf_counter
from numba import njit
import numpy as np

@njit(fastmath=True, cache=False)
def mult_matrix_with_numba(matrix_1, matrix_2):
    
    length = len(matrix_1) 
    result_matrix = [[0 for i in range(length)] for i in range(length)]

    for i in range(length):
        for j in range(length):
            for k in range(length):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return np.array(result_matrix)


def mult_matrix_without_numba(matrix_1, matrix_2):
    
    length = len(matrix_1) 
    result_matrix = [[0 for i in range(length)] for i in range(length)]

    for i in range(length):
        for j in range(length):
            for k in range(length):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return np.array(result_matrix)


if __name__ == "__main__":
    n = int(input("Введите размер матриц: "))
    matrix_1 = []

    print("Введите элементы первой матрицы построчно")
    for i in range(n):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        matrix_1.append(row)

    matrix_2 = []

    print("Введите элементы второй матрицы построчно")
    for i in range(n):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        matrix_2.append(row)

    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)

    start = perf_counter()
    res = mult_matrix_without_numba(matrix_1, matrix_2)
    end = perf_counter()
    print("Результат умножения:\n", res)    
    print("Время выполнения без numba: ", end - start)

    start = perf_counter()
    res = mult_matrix_with_numba(matrix_1, matrix_2)
    end = perf_counter()
    print("Время выполнения с numba: ", end - start)