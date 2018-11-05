# -*- coding: utf-8 -*-
import json
import ssl
from urllib import request

context = ssl._create_unverified_context()

with request.urlopen('https://api.douban.com/v2/book/2129650', context=context) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req, context=context) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

print('==============')

url = 'http://gw.sinochemb2c.com/auth/1.0.0/auth/login'
body = {"name": "18301138670", "code": "123456"}
headers = {'content-type': 'application/json'}

textmod = json.dumps(body).encode(encoding='utf-8')
req = request.Request(url=url, data=textmod, headers=headers)

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
