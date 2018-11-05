# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while True:
    # 发送数据:
    ins = input()
    if ins == 'exit':
        break
    s.send(bytes(ins, encoding='utf-8'))
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
