import socket,sys

ip = sys.argv[1]
ports = range(1,10000)

for port in ports:
    #print(port)
    sock = socket.socket()
    ret = sock.connect_ex((ip,port))
    if ret==0:
        print(str(port) + " open")
