import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 50000
sock.bind((host,port))
sock.listen(1)
print("Waiting connection ...")
connection,addr = sock.accept()
print("connection from :"+str(addr))
while True:
    data = connection.recv(1024)
    if data == b"exit":
        break
    print("Rev a massage :"+str(data))
    connection.send(data)
    print("sent a massage: "+str(data))
connection.close()
sock.close()
