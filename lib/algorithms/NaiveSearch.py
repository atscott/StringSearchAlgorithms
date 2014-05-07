from lib.algorithms.StringSearcher import StringSearcher

__author__ = 'https://github.com/ahelwer/IvoryTower/tree/master/string_algo'


class NaiveSearch(StringSearcher):
    def search(self, text, pattern):
        matches = []
        if len(pattern) == 0 or len(text) < len(pattern):
            return matches
        k = 0  # Alignment of P relative to T
        while k + len(pattern) <= len(text):
            i = 0  # Index to be compared
            while i < len(pattern) and pattern[i] == text[k + i]:
                i += 1
            if i == len(pattern):  # Match found
                matches.append(k)
            k += 1
        return matches