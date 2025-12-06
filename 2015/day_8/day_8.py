import os

file_path = os.path.join(os.path.dirname(__file__), 'day_8.txt')

with open(file_path, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    
str_len = 0
memory_len = 0

for line in lines:
    str_len += len(line)

    memory_len += len(eval(line))

result = str_len - memory_len
print(result)
