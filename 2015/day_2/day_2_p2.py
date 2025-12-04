import os

file_path = os.path.join(os.path.dirname(__file__), 'day_2.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

total_sqf = 0

for line in lines:
    dimensions = [int(x) for x in line.split('x')]
    l, w, h = dimensions
    dimensions.sort()
    
    wrap = 2 * (dimensions[0] + dimensions[1])
    bow = l * w * h
    
    total_sqf += bow + wrap

print(total_sqf)
