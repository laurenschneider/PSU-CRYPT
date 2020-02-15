# program to run the PSU CRYPT encryption step
# input is a 64 bit block. returns ciphertext

import whitening
import f


def encrypt(input):
    """
    :param input: 64 bit block
    :return: ciphertext
    """

    hexInput = ''.join([hex(ord(i)) for i in input]);
    inputList = [int(hexInput[i:i+4],16) for i in range(0, len(hexInput), 4)]

    key = 'aaaaaaaaaa'
    hexKey = ''.join([hex(ord(i)) for i in key]);
    keyList = [int(hexKey[i:i+4],16) for i in range(0, len(hexKey), 4)]

    # input whitening step
    res = whitening.whiten(inputList, keyList)

    # initalize each word of block for rounds. each of these are int
    rZero = res[0]
    rOne = res[1]
    rTwo = res[2]
    rThree = res[3]

    round = 0

    for i in range (0,15):
        rZeroTemp = rZero
        rOneTemp = rOne
        fZero, fOne = f.func(rZero,rOne,round)
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
    ciphertext, newKey = whitening.whiten([yZero, yOne, yTwo, yThree], key)

    return ciphertext
