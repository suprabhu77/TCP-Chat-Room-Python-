import socket

Mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
localhost = "127.0.0.1"
portaddress = 59000

Mysocket.bind((localhost,portaddress))
Mysocket.listen()

while True:
    clientsocket , address = Mysocket.accept()
    print(f"Connection established {address}")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
