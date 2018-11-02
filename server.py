#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json

dic = {}


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        x = False
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))
            sip = line.decode('utf-8').split(" ")
            if sip[1] != "\rn":
                if x is True:
                    if sip[1] == "0\r\n":
                        """
                        Caso en el que el Expired es 0
                        Elimino del diccionario la direccion
                        """
                        datos = {
                            'Sip': elemento,
                            'Ip': ip,
                            'Expires': sip[1]
                        }
                        with open('datos.json', 'w') as file:
                            json.dump(datos, file)
                        del dic[elemento]
                        print("Borrar cliente")
                        break
                    else:
                        print(sip[1])
                        """
                        Caso en el que el Expired es diferente a 0
                        """
                        datos = {
                            'Sip': elemento,
                            'Ip': ip,
                            'Expires': sip[1]
                        }
                        with open('datos.json', 'w') as file:
                            json.dump(datos, file)
                else:
                    elemento = sip[1]
                    ip = self.client_address[0]
                    """
                    Introduzco la direccion al diccionario
                    """
                    dic[elemento] = ip
                    x = True
        for key in dic:
            print(key + ":" + dic[key])


if __name__ == "__main__":
    """
    Listens at localhost ('') port introduced by keyboard
    and calls the EchoHandler class to manage the request
    """
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
