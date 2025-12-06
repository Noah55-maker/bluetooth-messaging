import random
import base64
from Crypto.Cipher import AES

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_GCM)

    nonce = bytes(cipher.nonce)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    return [nonce, ciphertext, tag]

def encryptString(message, key):
    b = bytearray()
    b.extend(map(ord, message))
    return encrypt(b, key)

def decrypt(key, nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        print("the message is authentic")
    except ValueError:
        print("Bad message")

    return plaintext

def decryptString(key, nonce, ciphertext, tag):
    return decrypt(key, nonce, ciphertext, tag).decode("utf-8")

key = bytearray(16)
for i in range(16):
    key[i] = random.randint(0, 255)

n, c, t = encryptString("Secret message", key)
print(decryptString(key, n, c, t))
