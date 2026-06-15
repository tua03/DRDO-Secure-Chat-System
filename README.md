# Secure Chat Application using RSA, AES and SHA-256

## Overview

This project implements a secure client-server chat application using Python socket programming. Two clients communicate through a central server while ensuring confidentiality and integrity of messages.

## Features

* Multi-client communication using TCP sockets
* RSA-based key exchange
* AES encryption for secure message transmission
* SHA-256 hashing for message integrity verification
* Multi-threaded clients for simultaneous sending and receiving
* Encrypted chat logging at the server

## Project Structure

* `server.py` – Handles client connections and message forwarding
* `client1.py` – First client implementation
* `client2.py` – Second client implementation
* `aes.py` – AES encryption and decryption functions
* `rsa.py` – RSA key generation and key exchange functions
* `sha.py` – SHA-256 hash generation
* `chat.log` – Stores encrypted chat logs

## Working

1. Client 1 generates an RSA public-private key pair.
2. The public key is shared with Client 2 through the server.
3. Client 2 generates an AES session key.
4. The AES key is encrypted using Client 1's RSA public key and transmitted.
5. Client 1 decrypts the AES key using its RSA private key.
6. Both clients now share the same AES session key.
7. Messages are hashed using SHA-256 and then encrypted using AES.
8. The server forwards encrypted messages and stores encrypted logs.
9. The receiving client decrypts the message and verifies its integrity using SHA-256.

## Security Mechanisms

### RSA

Used for secure exchange of the AES session key.

### AES

Used for encrypting chat messages to ensure confidentiality.

### SHA-256

Used to verify message integrity and detect tampering during transmission.

## Current Status

Implemented:

* Client-server communication
* RSA key exchange
* AES encryption/decryption
* SHA-256 integrity verification
* Encrypted logging

Future Enhancements:

* File transfer support
* Automatic client discovery
* Digital signatures for authentication

## Conclusion

The project demonstrates secure communication using a hybrid cryptographic approach where RSA is used for key exchange, AES for message encryption, and SHA-256 for integrity verification.
