#!/usr/bin/python

import socket

address = ("localhost", 20000)

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets
server_socket.bind(address)
server_socket.listen(1)
server_input, address = server_socket.accept()
print "Nova conexao recebida de ", address

# Print
while True:
    response = server_input.recv(1024)
    response = response.rstrip()
    if (response != "sair"):
		print "Mensagem do cliente:", response
    else:
		server_socket.close()
		break

