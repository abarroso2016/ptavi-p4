#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
#LINE = data = " ".join(sys.argv[4:])
LINE = sys.argv[4]
TIPO = sys.argv[3].upper()
EXPIRES = sys.argv[5]
TODO = TIPO + " sip:" + LINE + " SIP/2.0\r\n" + "Expires: " + EXPIRES


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", TODO)
    my_socket.send(bytes(TODO, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
