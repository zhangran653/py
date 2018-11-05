# -*- coding: utf-8 -*-

with open('/Users/zhangran/Desktop/Miss.Beauty and Toypoodle\'s Secret/To.Miss.Beauty.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
