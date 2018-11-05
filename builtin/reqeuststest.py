# -*- coding: utf-8 -*-
import json

import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)

url = 'http://gw.sinochemb2c.com/auth/1.0.0/auth/login'
body = {"name": "18301138670", "code": "123456"}
headers = {'content-type': 'application/json'}
textmod = json.dumps(body).encode(encoding='utf-8')
r = requests.post(url, data=textmod, headers=headers)
print(r.status_code)
print(r.text)
