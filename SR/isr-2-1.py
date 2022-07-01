def fibb(n):

    a, b = 1, 1

    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    n = int(input("Введите размер ряда: "))
    fibb_lst = list(fibb(n))
    print(fibb_lst)