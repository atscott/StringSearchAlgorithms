from lib.algorithms.BoyerMooreHorspool import BoyerMooreHorspool
from lib.algorithms.KnuthMorrisPratt import KnuthMorrisPratt
from lib.algorithms.NaiveSearch import NaiveSearch
from lib.algorithms.ZSearch import ZSearch
import time

__author__ = 'atscott'

current_milli_time = lambda: int(round(time.time() * 1000))


class StringSearchBenchmarker():
    def __init__(self):
        self.search_algorithms = [BoyerMooreHorspool(), KnuthMorrisPratt(),
                                  ZSearch()]
        self.various_sized_aesops = self.__generate_items_to_search()

    def benchmark(self):
        for text_to_search in self.various_sized_aesops:
            for algorithm in self.search_algorithms:
                start_time_in_millis = current_milli_time()
                locations = list(algorithm.search(text_to_search, 'themselves'))
                end_time_in_millis = current_milli_time()
                print(str(algorithm) + ': ' + str(end_time_in_millis - start_time_in_millis) + ", " + len(locations))

    def __generate_items_to_search(self):
        various_sized_aesops = []
        content = self.__get_aesop_file_contents()
        various_sized_aesops.append(content)
        for x in range(0, 200):
            various_sized_aesops.append(various_sized_aesops[-1] + content)
        return various_sized_aesops

    def __get_aesop_file_contents(self):
        f = open('aesop11.txt', 'r')
        content = f.read()
        f.close()
        return content

if __name__ == "__main__":
    StringSearchBenchmarker().benchmark()
