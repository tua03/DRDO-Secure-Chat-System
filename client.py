import socket
import threading
from aes import encrypt_message, decrypt_message
from sha import generate_hash

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

'''def receive():
    while True:
        ciphertext = client.recv(1024)

        if ciphertext:
            msg = decrypt_message(ciphertext)
            print("\nReceived:", msg)'''
def receive():
    while True:
        ciphertext = client.recv(1024)

        if ciphertext:

            packet = decrypt_message(ciphertext)

            msg, received_hash = packet.split("|||")

            new_hash = generate_hash(msg)

            if new_hash == received_hash:
                print("\nIntegrity Verified")
                print("Received:", msg)

            else:
                print("\nWARNING: Message Tampered!")

'''def send():
    while True:
        msg = input()
        encrypted = encrypt_message(msg)
        client.send(encrypted)'''
def send():
    while True:
        msg = input()

        # Generate SHA hash
        hash_value = generate_hash(msg)

        # Attach hash with message
        packet = msg + "|||" + hash_value

        # Encrypt complete packet
        encrypted = encrypt_message(packet)

        client.send(encrypted)
     

threading.Thread(target=receive).start()
threading.Thread(target=send).start()