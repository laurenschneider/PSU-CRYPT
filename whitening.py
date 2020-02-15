# first step of PSU CRYPT

def whiten(block, key):
    """
    :param block: list of four ints, 16 bits each
    :param key: list of five ints, 16 bits each
    :return: new list of four ints
    """
    result = []
    for i, word in enumerate(block):
        # xor word i and key i
        val = block[i] ^ key[i]
        result.append(val)

    # shift key
    """
    shiftedKey = []
    for i in range(0,4):
        shiftedKey.append(key[i+1])
    shiftedKey.append(key[0])
    """

    return result  #shiftedKey
