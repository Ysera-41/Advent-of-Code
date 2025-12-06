import os

file_path = os.path.join(os.path.dirname(__file__), 'day_7.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

ok = {}
pending = {}


def parse():
    for i in lines:
        parts = i.strip().split()
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
        
        pending[destino] = (operacao, operandos)


def operations():
    def pode(operandos):
        
        for op in operandos:
            if not (op.isdigit() or op in ok):
                return False
        return True
    
    def get_value(op):
        
        return int(op) if op.isdigit() else ok[op]
    
    while pending:
        executados = []
        
        for destino, (operacao, operandos) in list(pending.items()):
            
            if not pode(operandos):
                continue
            
            if operacao == 'ASSIGN':
                result = get_value(operandos[0])
            
            elif operacao == 'NOT':
                result = (~get_value(operandos[0])) & 0xFFFF
            
            elif operacao == 'AND':
                result = (get_value(operandos[0]) & get_value(operandos[1])) & 0xFFFF
            
            elif operacao == 'OR':
                result = (get_value(operandos[0]) | get_value(operandos[1])) & 0xFFFF
            
            elif operacao == 'LSHIFT':
                result = (get_value(operandos[0]) << get_value(operandos[1])) & 0xFFFF
            
            elif operacao == 'RSHIFT':
                result = (get_value(operandos[0]) >> get_value(operandos[1])) & 0xFFFF
            
            else:
                print("Operação desconhecida:", operacao)
                continue
            
            ok[destino] = result
            executados.append(destino)
        
        for d in executados:
            del pending[d]
        
        if not executados:
            print(f"Aviso: {len(pending)} instruções não processadas")
            break


parse()
operations()
valor_a_parte1 = ok['a']
print("Parte 1: valor de a =", valor_a_parte1)


ok.clear()
pending.clear()

parse()

pending['b'] = ('ASSIGN', [str(valor_a_parte1)])

operations()

print("Parte 2: novo valor de a =", ok['a'])