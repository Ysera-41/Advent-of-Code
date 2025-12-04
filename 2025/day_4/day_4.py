import os

file_path = os.path.join(os.path.dirname(__file__), 'day_4.txt')

with open(file_path, 'r') as file:
    lines = file.read().splitlines()
    
print(lines)
count = 0
# for i in line:
#
#     if i == '@':
#         count += 1
#         if count < 8:
#             continue
#         else:
#             count = 0
#             break
# print(i)