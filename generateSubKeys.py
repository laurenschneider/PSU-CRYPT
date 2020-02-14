import keySchedule

key = hex(0xabcdef0123456789abcd)

# 20 rounds, 12 subkeys per round

s1, key = keySchedule.kEncrypt(4*0, key)
s2, key = keySchedule.kEncrypt(4*0+1, key)
s3, key = keySchedule.kEncrypt(4*0+2, key)
s4, key = keySchedule.kEncrypt(4*0+3, key)

# note: kEncrypt returns strings!!!!
print(int(s1,16), ' ', s2, ' ', s3, ' ', s4)


"""
for round in range(0,20):
    roundKeys = []

    for j in range(0,3):

        subKey, key = keySchedule.kEncrypt(x,key)
"""
