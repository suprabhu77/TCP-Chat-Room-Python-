import socket
socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost = "127.0.0.1"
socketclient.connect((localhost, 59000))
msg = socketclient.recv(1024)
print(msg)