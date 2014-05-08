from lib.algorithms.StringSearcher import StringSearcher

__author__ = 'http://en.wikibooks.org/wiki/Algorithm_Implementation/String_searching/Knuth-Morris-Pratt_pattern_matcher'


class KnuthMorrisPratt(StringSearcher):
    def search(self, text, pattern):
        """Yields all starting positions of copies of the pattern in the text.
  Calling conventions are similar to string.find, but its arguments can be
  lists or iterators, not just strings, it returns all matches, not just
  the first one, and it does not need the whole text in memory at once.
  Whenever it yields, it will have read the text exactly up to and including
  the match that caused the yield."""

        # allow indexing into pattern and protect against change during yield
        pattern = list(pattern)

        # build table of shift amounts
        shifts = [1] * (len(pattern) + 1)
        shift = 1
        for pos in range(len(pattern)):
            while shift <= pos and pattern[pos] != pattern[pos - shift]:
                shift += shifts[pos - shift]
            shifts[pos + 1] = shift

        # do the actual search
        start_pos = 0
        match_len = 0
        for c in text:
            while match_len == len(pattern) or match_len >= 0 and pattern[match_len] != c:
                start_pos += shifts[match_len]
                match_len -= shifts[match_len]
            match_len += 1
            if match_len == len(pattern):
                yield start_pos

    def __str__(self):
        return 'Knuth Morris Pratt'
