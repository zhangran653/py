# -*- coding: utf-8 -*-

for x in range(9, 0, -1):
    for y in range(x, 0, -1):
        print(y, 'x', x, '=', x * y, '  ', end=' ')
    print()


def demoIterator():
    print("I'm in the first call of next()")
    yield 1
    print("I'm in the second call of next()")
    yield 3
    print("I'm in the third call of next()")
    yield 9

for i in demoIterator():
    print(i)

