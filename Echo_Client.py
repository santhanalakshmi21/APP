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

s.sendall('This will be sent to server')    # Send This message to server

data = s.recv(1024)	    # Now, receive the echoed
					    # data from server

print(data)				# Print received(echoed) data
s.close()				# close the connection