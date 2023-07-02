import socket
s = socket.socket()
host=socket.gethostname()
port = 4456
s.connect((host,port))
print("Client waiting for Connection")
s.send("request for conn".encode())
while True:
    data = s.recv(1024)
    if data.decode() == 'bye' or not data:
        break
    print("Server :" +data.decode())
    data = input("Client :")
    s.send(data.encode())
s.close()
