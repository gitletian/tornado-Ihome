# -*- coding: utf-8 -*-




class squares:
    def __init__(self, start, stop):
        self.flag = start - 1
        self.value = self.flag
        self.stop = stop

    def __iter__(self):
        self.value = self.flag
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value


a = squares(1, 5)

b = squares(1, 5)
s = 0

while s <= 41:
    for i in a:
        s = s + i
        print(s)

