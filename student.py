# -*- coding: utf-8 -*-


class Student(object):
    count = 0

    def __init__(self, name, score):
        self.score = score
        self.name = name

    def print_score(self):
        print('%s ,%s' % (self.score, self.name))

    def __getattr__(self, item):
        if item == 'age':
            return 34

    def __call__(self):
        print('%s %s' % (self.name, self.score))


lisa = Student('lisa', 98)
bart = Student('bart', 87)

lisa.print_score()
bart.print_score()
print(lisa.count)
lisa.count = 2
print(lisa.count)
print(Student.count)
print(dir(lisa))
a = lisa.age
print(a)
print(lisa.gender)

print(callable(lisa))

lisa()

print('=====')

print(type(lisa))
print(type(Student))


def f(self):
    print('fn...')


Hello = type('Hello', (object,), dict(fn=f, f2=f))

h = Hello()

h.fn()
h.f2()
print(type(Hello))
print(type(h))

list1 = [1]

list1.append(2)
print(list1)
lisa.a = 'asdf'
print(lisa.a)
