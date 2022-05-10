import socket
import sys
import threading

from sympy import C
import mmonitor


porta = int(input('Porta para ouvir sensores: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', porta))
except:
   print('# erro de bind')
   sys.exit()


c = threading.Thread( target=mmonitor.Console)
c.start()

s.listen(5)
 
print('aguardando sensores em ', porta)


while True:
    conn, addr = s.accept()
    print('recebi uma conexao de ', addr)

    t = threading.Thread( target=mmonitor.TrataSensor, args=(conn,addr,))
    t.start()

print('o servidor encerrou!')
s.close()