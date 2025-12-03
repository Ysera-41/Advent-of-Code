import os

file_path = os.path.join(os.path.dirname(__file__), 'day_1.txt')

s_pos = 50
count_zero = 0

with open(file_path, 'r') as file:
    instructions = file.readlines()

for line in instructions:
    line = line.strip()
    if not line:
        continue

    direction = line[0]
    moves = int(line[1:])

    if direction == 'R':
        s_pos = (s_pos + moves) % 100
    elif direction == 'L':
        s_pos = (s_pos - moves) % 100

    if s_pos == 0:
        count_zero += 1

print(count_zero)