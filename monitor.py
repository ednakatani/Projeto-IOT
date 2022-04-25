## Recebe as informações dos sensores

import socket
import sys
import threading


# === FUNÇÕES ===

def TrataSensor(conn):
    while True:
        data = conn.recv(1000)
        if not data:
            break
        else:
            print('recebi ', len(data), ' bytes')
            print(data)

    conn.close()    
    print('Sensor encerrado: ', conn)


# === PROGRAMA PRINCIPAL ===

HOST = ''       # ANY_IP = todos os IPs do HOST
SENSORES={}     # lista de sensores conectados
CONSOLE=None    # conexao com o console remoto

PORTA = int(input('Porta do servidor > '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORTA))
except:
   print('# erro de bind')
   sys.exit()

s.listen(2)

print('Aguardando conexoes porta: ', PORTA)


# === LOOP ===

while True:
    conn, addr = s.accept()
    print('Conexão recebida: ',)
    TrataSensor(conn) 
    print('Sensor encerrou a conexão')
    conn.close()
# === FIM LOOP ===


print('o servidor encerrou')
s.close()