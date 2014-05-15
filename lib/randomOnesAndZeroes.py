from random import Random

__author__ = 'atscott'

rand = Random()
f = open("onesAndZeroes.txt", "a+")
for i in range(0, 10000000):
    f.write(str(rand.randint(0, 1)))
    if i % 1000 == 0:
        f.write('\n')
f.close()
