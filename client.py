#!/usr/bin/python

import socket
import re



IP = "localhost"
PORT = 20000
DATA_SIZE = 2048
ENCODE_FORMAT = 'utf-8'

def main():
    address = (IP, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    print(f'\nConectado ao servidor {address}')

    # Echo
    while True:
        # Loop de leitura do protocolo
        full_protocol = ""
        text = input("\nInforme o protocolo ou digite '!SAIR' para desconectar: \n >")
        text = re.sub("\n",'',text)
        if (text == "!SAIR"):
            client_socket.send(text.encode(ENCODE_FORMAT))
            client_socket.close()
            break
        while(text.replace("\s",'') != ''):
            full_protocol = full_protocol + text +'\n'
            text = input(" >")
            #text = re.sub("\n",'',text)

        full_protocol = full_protocol + '\n'
        client_socket.send(full_protocol.encode(ENCODE_FORMAT))

        # O servidor irá retornar o status da operação
        status_response = client_socket.recv(DATA_SIZE).decode(ENCODE_FORMAT)
        status_response = status_response.rstrip()
        print(f'\n[Resposta] {status_response}')
        if status_response.split(' ')[0] == '200':
            # Código 200 representa que ocorreu tudo certo e a imagem será enviada
            filename = input("\nSalvar imagem como: ")
            img_file = open(f'{filename}.png','wb')
            # O servidor envia uma imagem que é maior que a capacidade de envio por meio
            # dos sockets (2048 bytes), por isso, quebramos a imagem em pedaços e enviamos.
            img_chunk = client_socket.recv(100000)
            img_file.write(img_chunk)
            img_file.close()
    print('\nConexão finalizada')


if __name__ == '__main__':
  main()
