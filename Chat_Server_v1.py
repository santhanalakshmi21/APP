# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:42:51 2020
@author: Admin
"""

#!usr/bin/python

import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object
s.bind((host,port))
s.listen(5)

print("Waiting for client...")
conn,addr = s.accept()	        # Accept connection when client connects
print("Connected by ", addr)

while True:
	data = conn.recv(1024)	    # Receive client data
	print('Client :'+data.decode())
	if data == 'quit' or not data:
		print("Server Exiting")
        break	        # exit from loop if no data
	data = input('Server:')
	conn.sendall(data.encode())	        # Send the received data back to client
conn.close()








