# program to run the PSU CRYPT encryption step
# input is a 64 bit block. returns ciphertext

import whitening
import keySchedule
import f


def encrypt(input):
    """
    :param input: 64 bit block
    :return: ciphertext
    """

    hexInput = ''.join([ "{:02x}".format(ord(i)) for i in input ])
    inputList = [int(hexInput[i:i+4],16) for i in range(0, len(hexInput), 4)]

    key = '0xabcdef0123456789abcd'          # get key in hex string
    key = key[2:]
    keyList = [int(key[i:i+4],16) for i in range(0, len(key), 4)]

    # input whitening step
    res = whitening.whiten(inputList, keyList)

    # initalize each word of block for rounds. each of these are int
    rZero = res[0]
    rOne = res[1]
    rTwo = res[2]
    rThree = res[3]

    # put key in correct format for keyschedule
    key = hex(int(key,16))

    for i in range (0,20):
        rZeroTemp = rZero
        rOneTemp = rOne
        subKeys, key = keySchedule.generateRoundKeys(i, key)
        fZero, fOne = f.func(rZero, rOne, i, subKeys)
        rZero = rTwo ^ fZero
        rOne = rThree ^ fOne
        rTwo = rZeroTemp
        rThree = rOneTemp


    # after last round, undo final swap
    yZero = rTwo
    yOne = rThree
    yTwo = rZero
    yThree = rOne

    # output whitening step
    finalInput = [yZero, yOne, yTwo, yThree]

    # get new key list for final whitening
    finalKey = key[2:]
    finalKeyList = [int(finalKey[i:i+4],16) for i in range(0, len(finalKey), 4)]

    ciphertextList = whitening.whiten(finalInput, finalKeyList)

    ciphertext = ""
    for i in range(0,len(ciphertextList)):
        h = hex(ciphertextList[i])
        h = h[2:]
        ciphertext = ciphertext + h

    return "0x" + ciphertext
