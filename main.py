# program to run the PSU CRYPT encryption scheme
import whitening
import f

# get input, will be in hex
input = 'the quick brown fox jumps over the lazy cat'.encode('utf-8')
input.hex()

# get key - 80 bits
key = 'aaaaaaaaaa'

# do for each 64 bit block of input:

# whitening step
whitening.whiten(input, key)

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
