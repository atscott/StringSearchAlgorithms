from lib.algorithms.BoyerMoore import BoyerMoore
from lib.algorithms.BoyerMooreHorspool import BoyerMooreHorspool
from lib.algorithms.KnuthMorrisPratt import KnuthMorrisPratt

__author__ = 'atscott'


class StringSearchBenchmarker():
    def __init__(self):
        self.horspool = BoyerMooreHorspool()
        self.pratt = KnuthMorrisPratt()
        self.moore = BoyerMoore()
