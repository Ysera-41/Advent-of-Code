import os

file_path = os.path.join(os.path.dirname(__file__), 'day_3.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

total_joltage = 0

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    posicao_atual = 0
    numero_final = ''
    
    if len(line) < 12:
        continue
    
    for k in range(12):
        digitos_restantes = 12 - (k + 1)
        
        limite_superior = len(line) - digitos_restantes
        
        maior_digito = '-1'
        indice_maior = -1
        
        for i in range(posicao_atual, limite_superior):
            if line[i] > maior_digito:
                maior_digito = line[i]
                indice_maior = i
        
        numero_final += maior_digito
        
        posicao_atual = indice_maior + 1
    
    total_joltage += int(numero_final)

print(total_joltage)