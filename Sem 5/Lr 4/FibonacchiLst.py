class FibonacchiLst:

    def __iter__(self):
        self.lst = [0, 1]
        return self

    def __next__(self):
        lst = self.lst
        self.lst.append(self.lst[-1] + self.lst[-2])
        return lst
