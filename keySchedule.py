# key schedule for PSU CRYPT

def leftRotate(bits):
    # bits must be int base 16
    # always rotates 80 bits by 1
    shifted = (bits << 1%80) & (2**80-1) | ((bits & (2**80-1)) >> (80-(1%80)))
    return hex(shifted)


def rightRotate(bits):
    # always rotates 80 bits by 1
    shifted = ((bits & (2**80-1)) >> 1%80) | (bits << (80-(1%80)) & (2**80-1))
    return hex(shifted)

def getByte(hexString, byteIndex):
    str = hexString[2:]
    subStr = str[-(byteIndex+1) * 2: len(str) - byteIndex * 2]
    return int(subStr, 16)


def kEncrypt(x, key):
    """
    :param x: some number
    :param key: the 80 bit key. must be hex()
    :return: 1 subkey, 1 byte long, in int
    :return: rotated key
    """
    # key is 10 bytes: k9,k8,k7,k6,k5,k4,k3,k2,k1,k0

    rotatedKey = leftRotate(int(key,16))        # left rotate key by 1 bit

    byteNum = x % 10                    # ex. byteNum = 2, byte k2

    return getByte(rotatedKey, byteNum), rotatedKey


def generateRoundKeys(round, key):
    """
    :param round: int
    :param key: 80 bit key in hex
    :return: list of 12 subkeys for the round. Each subkey 1 byte in int
    :return: last used key in hex string
    """

    subKeys = []

    for i in range(0,3):
        subKeyOne, key = kEncrypt(4*round, key)
        subKeyTwo, key = kEncrypt(4*round+1, key)
        subKeyThree, key = kEncrypt(4*round+2, key)
        subKeyFour, key = kEncrypt(4*round+3, key)
        subKeys.append(subKeyOne)
        subKeys.append(subKeyTwo)
        subKeys.append(subKeyThree)
        subKeys.append(subKeyFour)

    return subKeys, key
