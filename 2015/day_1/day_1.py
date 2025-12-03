import os

file_path = os.path.join(os.path.dirname(__file__), 'day_1.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

floor = 0

for line in lines:
    line = line.strip()

for i in line:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1

print(floor)