import sys
import encrypt

args = sys.argv

if len(args) > 1:
    if str(args[1]) == 'encrypt':
        pFile = open("plaintext.txt", "r")
        input = pFile.read()
        pFile.close()
        ciphertext = encrypt.encrypt(input)
        cFile = open("ciphertextResult.txt", "w")
        cFile.write(ciphertext)
        cFile.close()

    elif str(args[1]) == 'decrypt':
        print("decrption coming soon")
    else:
        print("invalid argument. Please use encrypt or decrypt")


else:
    print("Please use encrypt or decrypt as command line arg")
