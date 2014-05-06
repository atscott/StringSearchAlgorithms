__author__ = 'atscott'

from algorithms.StringSearcher import StringSearcher


class BoyerMooreHorspool(StringSearcher):
    def search(self, text, pattern):
        m = len(pattern)
        n = len(text)
        if m > n:
            return
        skip = []
        for k in range(256):
            skip.append(m)
        for k in range(m - 1):
            skip[ord(pattern[k])] = m - k - 1
        skip = tuple(skip)
        k = m - 1
        while k < n:
            j = m - 1
            i = k
            while j >= 0 and text[i] == pattern[j]:
                j -= 1
                i -= 1
            if j == -1:
                yield i + 1
            k += skip[ord(text[k])]