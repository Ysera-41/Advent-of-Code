import os

file_path = os.path.join(os.path.dirname(__file__), 'day_1.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

floor = 0
basement_position = None
position = 0

for line in lines:
    line = line.strip()
    
    for i in line:
        position += 1
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
        
        if floor == -1:
            basement_position = position
            break

# Print results
print(f"Final floor: {floor}")
if basement_position:
    print(f"First entered basement at position: {basement_position}")