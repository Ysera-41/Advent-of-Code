import os

file_path = os.path.join(os.path.dirname(__file__), 'day_8.txt')

with open(file_path, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

str_len = 0
encoded_len = 0

for line in lines:
    str_len += len(line)
    
    encoded = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
    encoded_len += len(encoded)

result = encoded_len - str_len
print(result)