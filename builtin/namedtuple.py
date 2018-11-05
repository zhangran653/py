# -*- coding: utf-8 -*-
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 3)
print(p)
print(p.x)
print(p.y)

