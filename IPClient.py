# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:43:18 2020
@author: Admin
"""
#!usr/bin/python
import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object
s.connect((host,port))
#s.sendall(b'Connection request')    # Send This message to server
while True:
    data = s.recv(1024)	    # Now, receive the echoed data from server
    print('Server : ' + data.decode())  # Print received(echoed) data
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    s.sendall(IPAddr.encode())
    print("Server :"+s.recv(1024).decode())
    break
s.close()				# close the connection