'''import hashlib

msg = input("Enter message: ")

hash_value = hashlib.sha256(msg.encode())

print("SHA-256 Hash:")
print(hash_value.hexdigest())
'''
import hashlib

def generate_hash(msg):
    return hashlib.sha256(msg.encode()).hexdigest()