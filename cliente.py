"""
Nombre: cliente.py
Objetivo: implementa un cliente con socket
Autor: tomado de https://realpython.com/python-sockets/
04/08/2020
"""

#!/usr/bin/env python3

import socket

HOST = '192.168.0.102'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola Mundo Peludo')
    data = s.recv(1024)

print('Received', repr(data))
