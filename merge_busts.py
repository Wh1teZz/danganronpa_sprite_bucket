import json

old = None
new = None

with open('busts.json', 'r') as f:
    old = json.load(f)

with open('new_busts.json', 'r') as f:
    new = json.load(f)

for k in new:
    old[k] = new[k]

with open('merged_busts.json', 'w') as f:
    json.dump(old, f)