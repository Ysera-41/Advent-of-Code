import os

file_path = os.path.join(os.path.dirname(__file__), 'day_5.txt')

with open(file_path, 'r') as file:
    lines = file.read().splitlines()

nice_words = 0

for word in lines:
    if sum(1 for char in word if char in 'aeiou') < 3:
        continue
    
    if not any(word[i] == word[i + 1] for i in range(len(word) - 1)):
        continue
    
    if any(forbidden in word for forbidden in ['ab', 'cd', 'pq', 'xy']):
        continue
    
    nice_words += 1

print(nice_words)