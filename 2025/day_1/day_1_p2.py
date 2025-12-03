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
        for i in range(1, moves + 1):
            new_pos = (s_pos + i) % 100
            if new_pos == 0:
                count_zero += 1
        s_pos = (s_pos + moves) % 100
    
    elif direction == 'L':
        for i in range(1, moves + 1):
            new_pos = (s_pos - i) % 100
            if new_pos == 0:
                count_zero += 1
        s_pos = (s_pos - moves) % 100

print(count_zero)