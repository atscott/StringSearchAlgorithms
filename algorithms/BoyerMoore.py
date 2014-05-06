from algorithms.StringSearcher import StringSearcher

__author__ = 'atscott'


class BoyerMoore(StringSearcher):
    def generate_bad_char_shift(self, term):
        skipList = {}
        for i in range(0, len(term) - 1):
            skipList[term[i]] = len(term) - i - 1
        return skipList

    # Generate the Good Suffix Skip List
    def find_suffix_position(self, bad_char, suffix, full_term):
        for offset in range(1, len(full_term) + 1)[::-1]:
            flag = True
            for suffix_index in range(0, len(suffix)):
                term_index = offset - len(suffix) - 1 + suffix_index
                if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                    pass
                else:
                    flag = False
            term_index = offset - len(suffix) - 1
            if flag and (term_index <= 0 or full_term[term_index - 1] != bad_char):
                return len(full_term) - offset + 1

    def generate_suffix_shift(self, key):
        skip_list = {}
        buffer = ""
        for i in range(0, len(key)):
            skip_list[len(buffer)] = self.find_suffix_position(key[len(key) - 1 - i],
                                                               buffer, key)
            buffer = key[len(key) - 1 - i] + buffer
        return skip_list

    # Actual Search Algorithm
    def search(self, text, pattern):
        global goodSuffixShift
        good_suffix = self.generate_suffix_shift(pattern)
        bad_char = self.generate_bad_char_shift(pattern)
        i = 0
        while i < len(text) - len(pattern) + 1:
            j = len(pattern)
            while j > 0 and pattern[j - 1] == text[i + j - 1]:
                j -= 1
            if j > 0:
                bad_char_shift = bad_char.get(text[i + j - 1], len(pattern))
                goodSuffixShift = good_suffix[len(pattern) - j]
                if bad_char_shift > goodSuffixShift:
                    i += bad_char_shift
                else:
                    i += goodSuffixShift
            else:
                yield i
                i += goodSuffixShift