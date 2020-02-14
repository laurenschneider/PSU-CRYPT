# F Function of the Feistel Cipher
import fTable

def concatBytes(b1, b2):
    """
    0xb1, 0xb2 hex strings
    :return: 0xb1b2 hex string
    """
    return hex((b1<<8) | b2)

def gFunc(rightBits, round, keys):
    """
    g func called from f func
    :param rightBits:
    :param round:
    :param keys:
    :return:
    """

    gOne = 1
    gTwo = 2

    # TODO get index for table

    gThree = fTable.getFromTable() ^ gOne
    gFour = fTable.getFromTable() ^ gTwo
    gFive = fTable.getFromTable() ^ gThree
    gSix = fTable.getFromTable() ^ gFour

    return concatBytes(gFive, gSix)

def func(rZero, rOne, round, subkeys):
    """
    :param rZero: 16 bit word R0
    :param rOne: 16 bit word R1
    :param round: current round number
    :param subKeys: dict of subkeys, should be 12 total. dict key corresponds to round
    :return: F0
    :return: F1
    """

    gKeys = null
    tZero = gFunc(rZero, round, gKeys)
    tOne = gFunc(rOne, round)
    cKeysOne = concatBytes()
    cKeysTwo = concatBytes()
    fZero = tZero + (2*tOne) + (cKeysOne % 65536)
    fOne = (2*tZero) + tOne + (cKeysTwo % 65536)


    return fZero, fOne
