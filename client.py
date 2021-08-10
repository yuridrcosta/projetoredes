#!/usr/bin/python

import socket

address = ("localhost", 20000)

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

# Echo
while True:
    text = raw_input("Informe texto ou digite 'sair' para desconectar: ")
    client_socket.send(text)
    if (text == "sair"):
        client_socket.close()
	break
