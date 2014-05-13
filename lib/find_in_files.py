from lib.algorithms.BoyerMooreHorspool import BoyerMooreHorspool

'''
Here's an example of how you could use knowledge about the best search algorithm to do something useful. If you were
searching for some text in your file system (like grep or agent ransack), then you could use these string search algos.
'''
__author__ = 'atscott'
import os

path = 'C:/'

totalSizeSearched = 0
for root, dirs, files in os.walk(path, False):
    for name in files:
        try:
            f = open(os.path.join(root, name), 'r')
            contents = f.read()
            totalSizeSearched += len(contents)
            if len(list(BoyerMooreHorspool().search(contents, 'java'))) > 0:
                print(os.path.join(root, name))
                print(totalSizeSearched)
        except IOError:
            f.close()
