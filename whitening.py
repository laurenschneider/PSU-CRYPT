# first step of PSU CRYPT

def whiten(block, key):
    """
    :param block: list of four 16 bit words
    :param key: list of five 16 bit words
    :return: new list of four 16 bit words
    :return: shifted key
    """
    result = []
    for i, word in enumerate(block):
        # xor word i and key i
        result.append(block[i] ^ key[i])

    # shift key
    shiftedKey = []
    for i in range(0,4):
        shiftedKey.append(key[i+1])
    shiftedKey.append(key[0])

    return result, shiftedKey
