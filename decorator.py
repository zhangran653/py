# -*- coding: utf-8 -*-
import functools
import time


def t1(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('%s %s:' % ('before ... ', fn.__name__))
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print('time:%s' % (end - start))
        return result

    return wrapper


@t1
def add(x, y):
    time.sleep(1)
    return x + y


s = add(2, 3)
print(s)


def d2(text):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print('%s %s:' % (text, fn.__name__))
            start = time.time()
            result = fn(*args, **kwargs)
            end = time.time()
            print('time:%s' % (end - start))
            return result

        return wrapper

    return decorator


@d2('lalala')
def mulitply(x, y):
    time.sleep(0.4)
    return x * y


s = mulitply(3, 7)
print(s)


def d3(*a):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print('%s %s:' % ('' if (a is None) else a[0], fn.__name__))
            start = time.time()
            result = fn(*args, **kwargs)
            end = time.time()
            print('time:%s' % (end - start))
            return result

        return wrapper

    return decorator


@d3('asdf')
def minus(x, y):
    time.sleep(0.1)
    return x - y


s = minus(6, 3)
print(s)
