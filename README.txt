Lauren Schneider
braun@pdx.edu

This program performs encryption of ASCII plaintext using the PSU-CRYPT encryption
scheme. Decryption is performed on a hex representation of ciphertext.

Requirements: Python3

To encrypt, modify the file "plaintext.txt" with your chosen message.
Enter your 80 bit key in the file "key.txt"
Run: python main.py encrypt
This will output ciphertext in 0x hex format in the file "ciphertextResult.txt"
To decrypt, enter the ciphertext into the file "ciphertext.txt" without "0x"
Run: python main.py decrypt
This will output the plaintext in the file "plaintextResult.txt"

Note: Plaintext and ciphertext must all be on one continuous line. Parsing for
encryption and decryption does not currently support newline characters.

Included files:
main.py
  Driver program. Takes an argument, "encrypt" or "decrypt"
encrypt.py
  This file runs all rounds of the block encryption and decryption.
f.py
  Module contains implementations of the f function and g function of the feistel round
fTable.py
  Includes the ftable data and method for retrieval.
keySchedule.py
  Module to generate the subkeys.
whitening.py
  Module to run the input and output whitening step
plaintext.txt
  Message to encrypt. Must all be on one line.
key.txt
  Key. Must be 80 bits.
ciphertext.txt
  Ciphertext for decryption. Must be hex form WITHOUT "0x"
plaintextResult.txt
  Output of running decryption
ciphertextResult.txt
  Output of running encryption
