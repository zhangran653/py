# -*- coding: utf-8 -*-
import functools


def count():
    fs = []
    for i in range(1, 4):
        j = i

        def f():
            return j * j

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1(), f2(), f3())

print(list(map(lambda x: x * x, range(1, 11))))


def log(func):
    def wapper(*args, **kwargs):
        print('before...', func.__name__)
        func(*args, **kwargs)

    return wapper


def now():
    print('2018-1-30')


print('=========')


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))

            func(*args, **kwargs)

        return wrapper

    return decorator


now = log1('erwse')(now)
now()
print(now.__name__)


