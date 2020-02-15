# first step of PSU CRYPT

def whiten(block, key):
    """
    :param block: list of four ints
    :param key: list of five ints
    :return: new list of four ints
    :return: shifted key in int
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
