import requests
import os
import json

basePath = os.getcwd()

data = None
with open('urls_out.json', 'r') as f:
    data = json.load(f)

if data == None:
    print('ayo wtf')
    exit()

for k in data:
    os.mkdir(k)
    os.chdir(basePath + '/' + k)
    print(os.getcwd())
    i = 0
    for url in data[k]:
        res = requests.get(url)
        with open(f'{k}_sprite_{i}.png', 'wb') as f:
            f.write(res.content)
        i += 1
    os.chdir(basePath)