#!/usr/bin/python

import socket
import threading
import imageProcessing
import protocol

IP = ""
PORT = 20000
DATA_SIZE = 2048
ENCODE_FORMAT = 'utf-8'

def handle_client(connection,address):
  print(f'Nova conexão recebida de {address}')
  while True:
    response = connection.recv(DATA_SIZE).decode(ENCODE_FORMAT)
    response = response.rstrip()
    if response == '!SAIR':
      break
    print(f'[{address}] {response}')
    person, message, status, color = protocol.parseProtocol(response)
    connection.send(status.encode(ENCODE_FORMAT))
    if (person == None and message == None):
      break
    imageProcessing.writeMessageInImage(person,message,color)
    
    img_file = open(f"serverside_IMG_{imageProcessing.getTemporaryId(person,message)}.png",'rb')
    img_data = img_file.read(DATA_SIZE)
    while img_data:
      connection.send(img_data)
      img_data = img_file.read(DATA_SIZE)

  connection.close()

def main():
  print('Servidor iniciado')
  address = (IP, PORT)
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

  server_socket.bind(address)
  server_socket.listen()

  while True:
    client_connection, client_address = server_socket.accept()
    thread = threading.Thread(target =handle_client,args=(client_connection,client_address))
    thread.start()
    print(f"Número de conexões ativas: {threading.activeCount()-1}")

if __name__ == '__main__':
  main()
