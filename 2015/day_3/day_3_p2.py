import os

file_path = os.path.join(os.path.dirname(__file__), 'day_3.txt')

with open(file_path, 'r') as file:
    lines = file.read()


santa_moves = lines[0::2]
sx, sy = 0, 0
robo_moves = lines[1::2]
rx, ry = 0, 0

houses = {(0, 0)}
for c in santa_moves:
    if c == '^':
        sy += 1
    elif c == 'v':
        sy -= 1
    elif c == '<':
        sx -= 1
    elif c == '>':
        sx += 1
    
    houses.add((sx, sy))

for k in robo_moves:
    if k == '^':
        ry += 1
    elif k == 'v':
        ry -= 1
    elif k == '<':
        rx -= 1
    elif k == '>':
        rx += 1
    
    houses.add((rx, ry))
    
print(len(houses))
