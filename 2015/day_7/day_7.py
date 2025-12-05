import os

file_path = os.path.join(os.path.dirname(__file__), 'day_7.txt')

with open(file_path, 'r') as file:
        lines = file.readlines()
        
ok = {}
pending = {}

def parse():
    for i in lines:
        
        parts = i.strip().split(' ')
        destino = parts[-1]
        
        if len(parts) == 3:
            operacao = 'ASSIGN'
            operandos = [parts[0]]
        
        elif len(parts) == 4:
            operacao = parts[0]
            operandos = [parts[1]]
            
        elif len(parts) == 5:
            operacao = parts[1]
            operandos = [parts[0], parts[2]]
            
        pending[destino] = [operacao, operandos]

def operations():
    
    def pode(operandos):
        for op in operandos:
            if not (op.isdigit() or op in ok):
                return False
        return True
            
parse()
operations()
print(ok)