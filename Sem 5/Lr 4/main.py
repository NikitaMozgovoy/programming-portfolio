from FibonacchiLst import FibonacchiLst


def fib(n):
    myiter = iter(FibonacchiLst())

    while (myiter.lst[-1] + myiter.lst[-2] <= n):
        next(myiter)
    return myiter.lst

    


if __name__ == "__main__":
    n = int(input())

    print(fib(n))

