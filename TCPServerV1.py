import socket
dns ={'google':'172.13.31.89','gmail':'154.32.176.11','w3school':'143.76.142.21'}
s = socket.socket()
host = socket.gethostname()
port = 4456
s.bind((host,port))
s.listen(5)
print('Server is listening')
conn, addr = s.accept()
print('connection accepted', addr)
while True:
    data = conn.recv(1024)
    if data.decode() == 'bye' or not data:
        break
    print("Client :"+data.decode())
    data =input('Server :')
    conn.sendall(data.encode())
conn.close()


