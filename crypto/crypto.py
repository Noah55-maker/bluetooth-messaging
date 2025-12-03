import random
from Crypto.Cipher import AES

def encrypt(message, key):
	cipher = AES.new(key, AES.MODE_GCM)

	nonce = cipher.nonce
	ciphertext, tag = cipher.encrypt_and_digest(message)
	return [nonce, ciphertext, tag]

def decrypt(key, nonce, ciphertext, tag):
	cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)

	try:
		cipher.verify(tag)
		print("the message is authentic")
	except ValueError:
		print("Bad message")

	return plaintext

key = bytearray(16)
for i in range(16):
	key[i] = random.randint(0, 255)

st = "This is my secret message"
b = bytearray()
b.extend(map(ord, st))
n, c, t = encrypt(b, key)

pt = decrypt(key, n, c, t)
print(pt.decode("utf-8"))
