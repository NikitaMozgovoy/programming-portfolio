import math

def squareSequenceDigit(n):
    x = 1
    while(True):
        s = str(x**2)
        if (len(s) < n):
            n -= len(s)
        else:
            return int(s[n-1])
        x += 1

if __name__ == "__main__":
    print(squareSequenceDigit(1))
    print(squareSequenceDigit(2))
    print(squareSequenceDigit(7))
    print(squareSequenceDigit(12))
    print(squareSequenceDigit(17))
    print(squareSequenceDigit(27))
