import unittest
from lib.algorithms.BoyerMooreHorspool import BoyerMooreHorspool
from lib.algorithms.KnuthMorrisPratt import KnuthMorrisPratt
from lib.algorithms.NaiveSearch import NaiveSearch
from lib.algorithms.ZSearch import ZSearch

__author__ = 'andrewscott'


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_text = "something that I'm searching that is in more than one place."
        self.horspool = BoyerMooreHorspool()
        self.pratt = KnuthMorrisPratt()
        self.naive = NaiveSearch()
        self.z = ZSearch()
        f = open('aesop11.txt', 'r')
        self.aesop = f.read()

    def test_knuth_morris_pratt_returns_correct_positions(self):
        locations = list(self.pratt.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_z_returns_correct_positions(self):
        locations = list(self.z.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_naive_search_returns_correct_positions(self):
        locations = list(self.naive.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_boyer_moore_horspool_returns_correct_positions(self):
        locations = list(self.horspool.search(self.test_text, "that"))
        self.assertEquals(locations, list((10, 29)))

    def test_boyer_moore_horsepool_no_results(self):
        locations = list(self.horspool.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_knuth_morris_pratt_no_results(self):
        locations = list(self.pratt.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_z_no_results(self):
        locations = list(self.z.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_naive_no_results(self):
        locations = list(self.naive.search(self.test_text, "asdf"))
        self.assertEquals(locations, list())

    def test_knuth_morris_pratt_returns_correct_size_from_aesop(self):
        locations = list(self.pratt.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)

    def test_boyer_moore_horsepool_returns_correct_size_from_aesop(self):
        locations = list(self.horspool.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)

    def test_naive_returns_correct_size_from_aesop(self):
        locations = list(self.naive.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)

    def test_z_returns_correct_size_from_aesop(self):
        locations = list(self.z.search(self.aesop, "that"))
        self.assertEquals(len(locations), 356)
