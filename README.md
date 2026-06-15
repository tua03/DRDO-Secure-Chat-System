# Secure Chat Application using AES and SHA-256

## Overview

This project implements a secure client-server chat application using Python sockets. Two clients can communicate through a server while maintaining message confidentiality and integrity.

## Features

* Multi-client communication using TCP sockets
* AES Encryption for message confidentiality
* SHA-256 Hashing for message integrity verification
* Encrypted chat logging on the server
* Multi-threaded client for simultaneous sending and receiving

## Project Structure

* `server.py` - Server implementation
* `client.py` - Client implementation
* `aes.py` - AES encryption and decryption
* `sha.py` - SHA-256 hash generation
* `rsa.py` - RSA demonstration
* `dh.py` - Diffie-Hellman demonstration
* `chat.log` - Encrypted message logs

## Working

1. Sender enters a message.
2. SHA-256 hash of the message is generated.
3. Message and hash are combined and encrypted using AES.
4. Server receives and forwards the encrypted message.
5. Server stores encrypted logs.
6. Receiver decrypts the message and verifies the SHA-256 hash.
7. If hashes match, message integrity is verified.

## Security Features

* **AES**: Provides confidentiality by encrypting messages.
* **SHA-256**: Detects message modification during transmission.
* **Encrypted Logs**: Server stores encrypted messages instead of plaintext.

## Future Enhancements

* RSA-based key exchange
* Automatic client discovery
* Digital signatures
* Group chat support

## Conclusion

The project demonstrates secure communication using Python sockets, AES encryption, and SHA-256 hashing while ensuring confidentiality and integrity of transmitted messages.
