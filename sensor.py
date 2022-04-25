## Envia os dados para o monitor

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = input('IP do servidor > ')
PORTA = int(input('Porta do servidor > '))
ID = input('ID do sensor > ')

try:
    s.connect((IP, PORTA))
except:
    print('Erro de conexão')

# Envia o ID automaticamente após a conexão
s.send(bytes(ID, 'utf-8'))

while True:
    try:
        line = input()
        if not line:
            print('Linha vazia encerra o programa')
            break
    except:
            print('programa abortado com CTRL+C')
    data = bytes(line, 'utf-8')
    tam = s.send(data)
           
    print('Enviado:  ',tam, 'bytes')
    print(data)