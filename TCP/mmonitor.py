CONSOLE = None
SENSORES = {}

def Console():
  global CONSOLE
  global SENSORES

  import socket
   
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.bind(('', 8888))
  except:
     print('# erro de bind')
     sys.exit()

  s.listen(1)

  while True:
    conn, addr = s.accept()
    print('console ativado ')
    CONSOLE = conn
   
    CONSOLE.send('Digite SENSOR_ID COMANDO\r\n'.encode()) 
    while True:
          data = CONSOLE.recv(200).decode()
          if not data:
            print('Console encerrou')
            CONSOLE = None
            break
          if(len(data) < 4):
            # ignorar quebras de linha do Putty
            continue
          try:
            (sensor, comando) = data.split(' ', 1)
            if sensor in SENSORES:
                SENSORES[sensor].send(comando.encode())
            else:
                CONSOLE.send('Esse sensor nao existe\r\n'.encode())
                print('Enviando lista sensores')

                CONSOLE.send('Sensores Cadastrados:\r\n'.encode())
                for sensor in SENSORES:
                  
                  CONSOLE.send(str('* '+sensor+'\r\n').encode())
                             
          except:
            CONSOLE.send('Digite SENSOR_ID COMANDO\r\n'.encode()) 
            print(data)


def TrataSensor(conn, addr):
  global CONSOLE  
  global SENSORES 
     
  # O sensor deve enviar seu ID apos a conexao
  sensor = conn.recv(10).decode()
  SENSORES[sensor] = conn

  print('o sensor ', sensor, ' registrado no socket', conn.getpeername())
 
  while True:
        try:
          data = conn.recv(100)
          if not data:
            break
          
          d = data.decode()
          print('sensor ', sensor, ' enviou ', d)
          
          if d == "ON":
            CONSOLE.send('Sensor ligado\r\n'.encode())
          else:
            CONSOLE.send('Sensor desligado\r\n'.encode())
          

        except:
          break
       
  conn.close()     
  print('O sensor ', sensor, ' encerrou')
  SENSORES.pop(sensor)