import socket
import threading
from aes import encrypt_message, decrypt_message
from sha import generate_hash
from rsa import *
from Crypto.PublicKey import RSA

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))
private_key, public_key = generate_keys()

public_pem = public_key.export_key()

client.send(public_pem)

print("Public Key Sent")

encrypted_aes_key = client.recv(4096)

aes_key = decrypt_key(encrypted_aes_key, private_key)

print("Recovered AES Key:")
print(aes_key)

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

            packet = decrypt_message(ciphertext , aes_key)

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
        encrypted = encrypt_message(packet , aes_key)

        client.send(encrypted)
     

threading.Thread(target=receive).start()
threading.Thread(target=send).start()