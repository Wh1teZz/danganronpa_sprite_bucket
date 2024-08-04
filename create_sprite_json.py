import os
import json

baseDir = os.getcwd()

ignore = [
    '.git',
    'create_sprite_json.py',
    'sprite_downloader.py',
    'urls_out.json'
]

out = {}

for dir in os.listdir():
    if dir in ignore:
        continue
    
    out[dir] = []

    os.chdir(baseDir + '\\' + dir)

    for file in os.listdir():
        out[dir].append(f'https://raw.githubusercontent.com/Wh1teZz/danganronpa_sprite_bucket/master/{dir}/{file}')

    os.chdir(baseDir)

with open('new_busts.json', 'w') as f:
    json.dump(out, f)