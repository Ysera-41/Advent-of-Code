import os

file_path = os.path.join(os.path.dirname(__file__), 'day_2.txt.txt')

with open(file_path, 'r') as file:
    inputs = file.readlines()

id = inputs[0].strip().split(',')
invalid_id = 0

for i in range(len(id)):
    s, f = id[i].split('-')
    
    for j in range(int(s) , int(f) + 1):
        s_j = str(j)
        L = len(s_j)
        
        found = False
        for k in range(1, L // 2 + 1):
            if L % k == 0:
                bloco = s_j[:k]
                if bloco * (L // k) == s_j:
                    invalid_id += j
                    found = True
                    break
                    
print(invalid_id)