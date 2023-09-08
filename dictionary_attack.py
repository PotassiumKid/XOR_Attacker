ciphertext = "2c11130b59130b591b582a1f1b0b1f0c59371d0a09191e1f"
ciphertext_bytes = bytes.fromhex(ciphertext)

with open("wordlist.txt", "r") as file:
	for line in file:
		key = line.strip().encode()
		decrypted = bytearray()

		for i in range(len(ciphertext_bytes)):
			decrypted.append(ciphertext_bytes[i] ^ key[i % len(key)])
		if all(32 <= byte <= 126 for byte in decrypted):
			print("Trying: " + line)
			print("Decrypted (ASCII)", decrypted.decode())
