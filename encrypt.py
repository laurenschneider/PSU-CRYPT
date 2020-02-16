# program to run the PSU CRYPT encryption step
# input is a 64 bit block. returns ciphertext

import whitening
import keySchedule
import f

def feistel(res, allSubKeys):
    # initalize each word of block for rounds. each of these are int
    rZero = res[0]
    rOne = res[1]
    rTwo = res[2]
    rThree = res[3]

    for i in range (0,20):
        rZeroTemp = rZero
        rOneTemp = rOne
        fZero, fOne = f.func(rZero, rOne, i, allSubKeys[i])
        rZero = rTwo ^ fZero
        rOne = rThree ^ fOne
        rTwo = rZeroTemp
        rThree = rOneTemp

    return rZero, rOne, rTwo, rThree

def blockEncrypt(input, key, allSubKeys):
    """
    :param input: 64 bit block in form of int list
    :param key: 80 bit key in string
    :param allSubKeys: list of all needed subkeys
    :return: ciphertext
    """

    key = key[2:22]
    keyList = [int(key[i:i+4],16) for i in range(0, len(key), 4)]

    # input whitening step
    res = whitening.whiten(input, keyList)

    # rounds
    rZero, rOne, rTwo, rThree = feistel(res, allSubKeys)

    # after last round, undo final swap
    yZero = rTwo
    yOne = rThree
    yTwo = rZero
    yThree = rOne

    # output whitening step
    finalInput = [yZero, yOne, yTwo, yThree]

    # get new key list for final whitening
    print(key)
    finalKeyList = [int(key[i:i+4],16) for i in range(0, len(key), 4)]

    ciphertextList = whitening.whiten(finalInput, finalKeyList)

    ciphertext = ""
    for i in range(0,len(ciphertextList)):
        h = hex(ciphertextList[i])
        h = h[2:]
        ciphertext = ciphertext + h

    return ciphertext


def encrypt(input, key, flag):
    """
    :param input: some string input of any length
    :param key: hex string
    :param flag: 0 means encrypt, 1 means decrypt
    :return: final ciphertext hex string
    """

    # generate all needed subkeys, 12 per each 20 rounds. list of lists
    allKeys = []
    for i in range(0,20):
        subKeys, key = keySchedule.generateRoundKeys(i, key)
        allKeys.append(subKeys)

    # split after newline char
    res = input.split('\n')
    input = res[0]

    result = ''

    if flag == 0:       # encrypt

        # need 64 bit blocks, add padding if necessary
        if (len(input) % 8) != 0:
            print("adding padding to input")
            print(input)
            r = len(input) % 8
            for i in range(0,8-r):
                input = input + ' '

        # split into list of 64 bit strings
        blocks = [input[i:i+8] for i in range(0, len(input), 8)]

        # call block encryption on each block
        ciphertext = '0x'
        for i in range(0, len(blocks)):

            # format the first block to list form
            hexInput = ''.join([ "{:02x}".format(ord(i)) for i in blocks[i] ])
            inputList = [int(hexInput[i:i+4],16) for i in range(0, len(hexInput), 4)]

            c = blockEncrypt(inputList, key, allKeys)
            ciphertext = ciphertext + c

        result = ciphertext

    elif flag == 1:     # decrypt
        # get keys reversed
        revKeys = allKeys[::-1]

        # need 64 bit blocks, cut off extra
        if (len(input) % 16) != 0:
            r = len(input) % 16
            end = len(input) - r
            input = input[:end]

        # split into list of 64 bit strings, 8 bytes, so 8 hex pairs
        blocks = [input[i:i+16] for i in range(0, len(input), 16)]

        plaintext = ''
        for i in range(0, len(blocks)):
            # format first block to list of four ints
            cInput = blocks[i]
            inputList = [int(cInput[j:j+4],16) for j in range(0, len(cInput), 4)]

            p = blockEncrypt(inputList, key, revKeys)
            plaintext = plaintext + p

        result = bytes.fromhex(plaintext).decode("ASCII")

    return result
