import unittest
from lib.algorithms.BoyerMoore import BoyerMoore
from lib.algorithms.BoyerMooreHorspool import BoyerMooreHorspool
from lib.algorithms.KnuthMorrisPratt import KnuthMorrisPratt

__author__ = 'andrewscott'


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_text = "something that I'm searching that is in more than one place."
        self.horspool = BoyerMooreHorspool()
        self.pratt = KnuthMorrisPratt()
        self.moore = BoyerMoore()
        f = open('aesop11.txt', 'r')
        self.aesop = f.read()

    def test_knuth_morris_pratt_multiple_results(self):
        locations = list(self.pratt.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_boyer_moore_horspool_multiple_results(self):
        locations = list(self.horspool.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_boyer_moore_multiple_results(self):
        locations = list(self.moore.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_boyer_moore_no_results(self):
        locations = list(self.moore.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_boyer_moore_horsepool_no_results(self):
        locations = list(self.horspool.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_knuth_morris_pratt_no_results(self):
        locations = list(self.pratt.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_knuth_morris_pratt_returns_correct_size_from_aesop(self):
        locations = list(self.pratt.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)

    def test_boyer_moore_returns_correct_size_from_aesop(self):
        locations = list(self.moore.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)

    def test_boyer_moore_horsepool_returns_correct_size_from_aesop(self):
        locations = list(self.horspool.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)
