from algorithms.BoyerMoore import BoyerMoore
from algorithms.BoyerMooreHorspool import BoyerMooreHorspool
from algorithms.KnuthMorrisPratt import KnuthMorrisPratt

__author__ = 'andrewscott'
# Knuth-Morris-Pratt string matching
# David Eppstein, UC Irvine, 1 Mar 2002
# from http://code.activestate.com/recipes/117214/


kmp = KnuthMorrisPratt()
theText = "something that I'm searching that is in more than one place."
locations = kmp.search(theText, "that")
for location in locations:
    print(location)
bmh = BoyerMooreHorspool()
locations2 = bmh.search(theText, "that")
for location in locations2:
    print(location)
bm = BoyerMoore()
locations3 = bm.search(theText, "that")
for location in locations3:
    print(location)