import socket
s = socket.socket()
host = socket.gethostname()
port = 6543

s.connect((host,port))
s.sendall("Client request for connection".encode())
while True:
	data = s.recv(1024)
	if data.decode() == 'quit' or not data:
		break
	else:
		print('server :'+data.decode())
		st = input('Client :')
		s.sendall(st.encode())
s.close()