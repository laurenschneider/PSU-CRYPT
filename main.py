import sys
import encrypt

args = sys.argv

if len(args) > 1:
    if str(args[1]) == 'encrypt':
        pFile = open("plaintext.txt", "r")
        input = pFile.read()
        pFile.close()

        kFile = open("key.txt", "r")
        key = kFile.read()
        kFile.close()

        ciphertext = encrypt.encrypt(input, key, 0)

        cFile = open("ciphertextResult.txt", "w")
        cFile.write(ciphertext)
        cFile.close()

    elif str(args[1]) == 'decrypt':
        cFile = open("ciphertext.txt", "r")
        input = cFile.read()
        cFile.close()

        kFile = open("key.txt", "r")
        key = kFile.read()
        kFile.close()

        plaintext = encrypt.encrypt(input, key, 1)

        pFile = open("plaintextResult.txt", "w")
        pFile.write(plaintext)
        pFile.close()

    else:
        print("invalid argument. Please use encrypt or decrypt")


else:
    print("Please use encrypt or decrypt as command line arg")
