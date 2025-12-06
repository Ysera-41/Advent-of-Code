import os

file_path = os.path.join(os.path.dirname(__file__), 'day_9.txt')

with open(file_path, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

distances = {}
cities = set()

def parse():
    for line in lines:
        
        parts = line.split()
        city1, city2, distance = parts[0], parts[2], int(parts[4])
        
        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance
        
        if city1 not in cities or city2 not in cities:
            cities.add(city1)
            cities.add(city2)

