'''
Q.10  Implement a stand-alone sender receiver
program in which Sender encrypts a given text
message entered from keyboard in a byte-by-
byte manner using RC4 Stream Cipher and
transmits it to receiver. Receiver Decrypts the
ciphertext displays the decrypted contents on
screen. Use Appropriate package/Library for
RC4.
'''

#pip install receiver
from Crypto.Cipher import ARC4

def receiver():
    with open('encrypted_message.bin', 'rb') as f:
        ciphertext = f.read()

    key = input("Enter the secret key (password) used for encryption: ").encode()

    cipher = ARC4.new(key)

    plaintext = cipher.decrypt(ciphertext)

    print("Decrypted message:", plaintext.decode())

if __name__ == "__main__":
    receiver()