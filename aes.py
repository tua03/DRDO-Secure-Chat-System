'''from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'

def encrypt_message(msg):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return encrypted
def decrypt_message(encrypted):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode()
    

'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_message(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return encrypted

def decrypt_message(encrypted, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode()