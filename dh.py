p = 23
g = 5

a = 6
b = 15

A = (g ** a) % p
B = (g ** b) % p

key_alice = (B ** a) % p
key_bob = (A ** b) % p

print("Alice Public Key:", A)
print("Bob Public Key:", B)

print("Shared Secret (Alice):", key_alice)
print("Shared Secret (Bob):", key_bob)
