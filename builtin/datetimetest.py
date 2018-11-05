# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(type(now))
print(now.date())

dt = datetime(2018, 11, 2, 12, 34, 45, 4)
print(dt)

print(dt.timestamp())

t = 1429417200.0

print(datetime.fromtimestamp(t))

cday = datetime.strptime('2018-11-3 12:34:45', '%Y-%m-%d %H:%M:%S')
print(cday)

print(cday.strftime('%Y-%m-%d'))
print(cday + timedelta(hours=10))

