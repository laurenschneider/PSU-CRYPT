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
    return hex(int(subStr, 16))


def kEncrypt(x, key):
    """
    :param x: some number
    :param key: the 80 bit key. must be hex()
    :return: 1 subkey, 1 byte long, in hex
    :return: rotated key
    """
    # key is 10 bytes: k9,k8,k7,k6,k5,k4,k3,k2,k1,k0

    rotatedKey = leftRotate(int(key,16))        # left rotate key by 1 bit

    byteNum = x % 10                    # ex. byteNum = 2, byte k2

    return getByte(rotatedKey, byteNum), rotatedKey


def kDecrypt(x, key):
    """
    :param x: some number
    :param key: the 80 bit key
    :return: x mod 10 byte of the key K’
    """

    pass
