#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

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
                if x == True:
                    if sip[1] == "0\r\n":
                        del dic[elemento]
                        print("Borrar cliente")
                        break
                    else:
                        print(sip[1])
                else:
                    elemento = sip[1]
                    dic[elemento] = self.client_address[0]
                    x = True
        for key in dic:
            print(key + ":" + dic[key])

if __name__ == "__main__":
    # Listens at localhost ('') port 6001 
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler) 

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
