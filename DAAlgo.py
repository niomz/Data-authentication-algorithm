p = 23
q = 11
g = 4

private_key = 3
k = 7
message = input("Enter message: ")
h = sum(ord(ch) for ch in message) % q
public_key = pow(g, private_key, p)

r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h + private_key * r)) % q
print("Signature:", r, s)

w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = (pow(g, u1, p) * pow(public_key, u2, p) % p) % q

if r != 0 and s != 0 and v == r:
  print("Signature is valid")
else:
  print("Signature is invalid")