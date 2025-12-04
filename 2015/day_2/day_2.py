import os

file_path = os.path.join(os.path.dirname(__file__), 'day_2.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()
    
total_sqf = 0

for line in lines:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)

    a1 = l * w
    a2 = w * h
    a3 = h * l
    
    result = (2 * a1) + (2 * a2) + (2 * a3) + min(a1, a2, a3)
    total_sqf += result
    
print(total_sqf)
