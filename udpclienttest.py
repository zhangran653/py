# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    # 发送数据:
    ins = input()
    if ins == 'exit':
        break
    s.sendto(bytes(ins, encoding='utf-8'), ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
