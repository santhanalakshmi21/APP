import socket
s = socket.socket()
host = socket.gethostname()
port = 6543
s.bind((host, port))
s.listen(5)
print('Server Waiting for Client')
conn, addr = s.accept()
print("Connection accepted from ",addr)
while True:
    data = conn.recv(1024)
    if data.decode() == 'quit' or not data:
        break
    print('Client :'+data.decode())
    data = input('Server :')
    conn.sendall(data.encode())
conn.close()

