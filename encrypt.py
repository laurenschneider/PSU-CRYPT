# program to run the PSU CRYPT encryption step
# input is a 64 bit block. returns ciphertext

import whitening
import f


def encrypt(input):
    """
    :param input: 64 bit block
    :return: ciphertext
    """

    input.hex()

    # get key - 80 bits
    key = 'aaaaaaaaaa'

    # do for each 64 bit block of input:

    # input whitening step
    res, newKey = whitening.whiten(input, key)

    # initalize each word of block for rounds
    rZero = 1   # TODO - placeholder
    rOne = 2
    rTwo = 3
    rThree = 4

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
