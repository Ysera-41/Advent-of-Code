import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'day_6.txt')

with open(file_path, 'r') as file:
    lines = file.read().splitlines()

lights = np.full((1000, 1000), False, dtype=bool)

for line in lines:
    parts = line.split()

    if parts[0] == 'toggle':
        ac = 'toggle'
        c1 = parts[1]
        c2 = parts[3]
    else:
        ac = parts[1]
        c1 = parts[2]
        c2 = parts[4]

    x1, y1 = map(int, c1.split(','))
    x2, y2 = map(int, c2.split(','))

    yf = slice(y1, y2 + 1)
    xf = slice(x1, x2 + 1)

    if ac == 'on':
        lights[yf, xf] = True
    elif ac == 'off':
        lights[yf, xf] = False
    elif ac == 'toggle':
        lights[yf, xf] = ~lights[yf, xf]

total = lights.sum()
print(total)