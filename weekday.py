from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sat.value)
print(Weekday(1))
print(Weekday(0) == Weekday.Sun)
print(Weekday(2) == 2)
print(Weekday(2) == Weekday.Tue)
