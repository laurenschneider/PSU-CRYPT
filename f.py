# F Function of the Feistel Cipher
import fTable

def concatBytes(b1, b2):
    """
    0xb1, 0xb2 hex strings in int, 8 bits each
    :return: 0xb1b2 hex, return in int 16 bits
    """
    return (b1<<8) | b2

def gFunc(r, round, keys):
    """
    g func called from f func
    :param r: int, 16 bits
    :param round: int
    :param keys: list of 4 keys, 4 ints
    :return: 16 bit int
    """

    gOne = r >> 8               # get 8 high bits
    b = format(r, '016b')       # make sure to have 16 bit bin str
    bLow = b[8:]                        # get only 8 low bits
    gTwo = int(bLow, 2)                 # convert back to int from base 2

    print("g1 :", hex(gOne))
    print("g2 :", hex(gTwo))
    gThree = fTable.getFromTable(gTwo^keys[0]) ^ gOne
    print("g3 :", hex(gThree))
    gFour = fTable.getFromTable(gThree^keys[1]) ^ gTwo
    print("g4 :", hex(gFour))
    gFive = fTable.getFromTable(gFour^keys[2]) ^ gThree
    print("g5: ", hex(gFive))
    gSix = fTable.getFromTable(gFive^keys[3]) ^ gFour
    print("g6: ", hex(gSix))
    return concatBytes(gFive, gSix)

def func(rZero, rOne, round, subKeys):
    """
    :param rZero: int
    :param rOne: int
    :param round: current round number
    :param subKeys: list of subkeys, should be 12 total
    :return: F0 int
    :return: F1 int
    """

    tZero = gFunc(rZero, round, subKeys[0:4])               # need four keys
    tOne = gFunc(rOne, round, subKeys[4:8])                 # need four keys

    print("t0: ", hex(tZero))
    print("t1: ", hex(tOne))

    cKeysOne = concatBytes(subKeys[8], subKeys[9])          # need two keys
    cKeysTwo = concatBytes(subKeys[10], subKeys[11])        # need two keys
    fZero = (tZero + (2*tOne) + cKeysOne) % 65536
    fOne = ((2*tZero) + tOne + cKeysTwo) % 65536


    return fZero, fOne
