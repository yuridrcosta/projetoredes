#!/usr/bin/python

import socket

IP = "localhost"
PORT = 20000
DATA_SIZE = 2048

def main():
    address = (IP, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Conectado ao servidor {address}')
    client_socket.connect(address)

    # Echo
    while True:
        text = raw_input("Informe texto ou digite '!SAIR' para desconectar: ")
        client_socket.send(text)

        if (text == "!SAIR"):
            client_socket.close()
            break

        filename = input("Salvar imagem como: ")
        img_file = open(f'{filename}.png','wb')
        # O servidor envia uma imagem que é maior que a capacidade de envio por meio
        # dos sockets (2048 bytes), por isso, quebramos a imagem em pedaços e enviamos.

        img_chunk = client_socket.recv(DATA_SIZE)
        while img_chunk:
            img_file.write(img_chunk)
            img_chunk = client_socket.recv(DATA_SIZE)
        img_file.close()



if __name__ == '__main__':
  main()
