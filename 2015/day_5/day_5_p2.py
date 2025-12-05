import os

file_path = os.path.join(os.path.dirname(__file__), 'day_5.txt')

with open(file_path, 'r') as file:
    lines = file.read().splitlines()

def has_repeated_pair(word):
    for i in range(len(word) - 1):
        pair = word[i:i+2]
        if pair in word[i+2:]:
            return True
    return False

def has_repeat_with_one_between(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False

nice_words = 0

for word in lines:
    if not has_repeated_pair(word):
        continue

    if not has_repeat_with_one_between(word):
        continue

    nice_words += 1

print(nice_words)
