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
s.sendall(b'This will be sent to server')    # Send This message to server
while True:

    data = s.recv(1024)	    # Now, receive the echoed data from server
    if not data or data == 'quit':
        break
    else:
        print('echoed '+data.decode()) # Print received(echoed) data
        st = input('Client : ')
        s.sendall(st.encode())
s.close()				# close the connection