import socket
import threading
from aes import encrypt_message, decrypt_message
from sha import generate_hash
from rsa import *
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))
public_pem = client.recv(4096)

public_key = RSA.import_key(public_pem)

print("Public Key Received")

aes_key = get_random_bytes(16)

print("Generated AES Key:")
print(aes_key)

encrypted_aes_key = encrypt_key(aes_key, public_key)

client.send(encrypted_aes_key)

print("Encrypted AES Key Sent")

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