import os

file_path = os.path.join(os.path.dirname(__file__), 'day_2.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()
    
for line in lines:
    print(line)