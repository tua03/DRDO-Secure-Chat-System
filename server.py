import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen(2)

print("Waiting for clients...")

client1, addr1 = server.accept()
print("Client1 connected")

client2, addr2 = server.accept()
print("Client2 connected")

while True:
    
    msg = client1.recv(1024)

    if msg:
        with open("chat.log", "a") as f:
            f.write("Client1: " + msg.hex() + "\n")
        client2.send(msg)

    msg = client2.recv(1024)
    if msg:
        with open("chat.log", "a") as f:
            f.write("Client2: " + msg.hex() + "\n")
        client1.send(msg)