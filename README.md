# Secure Chat Application using AES and SHA-256

## Project Overview

This project implements a secure client-server chat application using Python sockets. Two clients can communicate through a server while maintaining confidentiality and integrity of messages.

## Features

* Multi-client communication using TCP sockets
* AES Encryption for message confidentiality
* SHA-256 Hashing for message integrity verification
* Multi-threaded client for simultaneous sending and receiving
* Encrypted chat logging at the server side

## Project Structure

server.py - Server implementation

client.py - Client implementation

aes.py - AES encryption and decryption functions

sha.py - SHA-256 hash generation functions

chat.log - Encrypted message logs

## Working

1. The sender enters a message.
2. SHA-256 hash of the message is generated.
3. The message and hash are combined.
4. The combined packet is encrypted using AES.
5. The encrypted packet is sent to the server.
6. The server stores encrypted logs
