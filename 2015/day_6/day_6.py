import numpy as np
import os

from numpy.ma.core import maximum

file_path = os.path.join(os.path.dirname(__file__), 'day_6.txt')

with open(file_path, 'r') as file:
    lines = file.read().splitlines()

lights = np.zeros((1000, 1000))
total = 0
for line in lines:
    parts = line.split()
    
    if parts[0] == 'toggle':
        c1 = parts[1]
        c2 = parts[3]
        ac = 'toggle'
    else:
        ac = parts[1]
        c1 = parts[2]
        c2 = parts[4]
        
    x1, y1 = map(int, c1.split(','))
    x2, y2 = map(int, c2.split(','))
    
    yf = slice(y1, y2 + 1)
    xf = slice(x1, x2 + 1)
    
    if ac == 'on':
        lights[yf, xf] += 1
    elif ac == 'off':
        lights[yf, xf] = maximum(0, lights[yf, xf] - 1)
    else:
        lights[yf, xf] += 2

total = lights.sum()
print(total)