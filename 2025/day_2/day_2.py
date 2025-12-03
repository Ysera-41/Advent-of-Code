import os

file_path = os.path.join(os.path.dirname(__file__), 'day_2.txt.txt')

with open(file_path, 'r') as file:
    inputs = file.readlines()

id = inputs[0].strip().split(',')
ivalid_id = 0

for i in range(len(id)):
    s, f = id[i].split('-')
    
    for j in range(int(s) , int(f) + 1):
        s_j = str(j)
        
        if len(s_j) % 2 != 0:
            continue
        
        mid = len(s_j) // 2
        left = s_j[:mid]
        right = s_j[mid:]
        
        if left == right:
            ivalid_id += j
    
print(ivalid_id)