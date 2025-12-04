import os

file_path = os.path.join(os.path.dirname(__file__), 'day_3.txt')

with open(file_path, 'r') as file:
    lines = file.read()
    
x = 0
y = 0
house = {(0,0):1}
total = 0

for c in lines:
    
    if c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    elif c == '<':
        x -= 1
    elif c == '>':
        x += 1

    house[(x,y)] = house.get((x,y), 0) + 1

total = len(house.items())
print(total)

    