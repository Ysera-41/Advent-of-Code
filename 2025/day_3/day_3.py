import os

file_path = os.path.join(os.path.dirname(__file__), 'day_3.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

total_joltage = 0

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    max_joltage = 0
    
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            num = (int(line[i]) * 10) + int(line[j])
            if num > max_joltage:
                max_joltage = num
    
    total_joltage += max_joltage

print(total_joltage)