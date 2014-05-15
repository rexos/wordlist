# -*- coding: utf-8 -*-
############################################
#                                          #
# Wordlist generator, creates dictionaries #
# Developed by rexos.                      #
# Code and performance optimisation by     #
# dbonadiman.                              #
#                                          #
############################################
"""Wordlist

Generates all possible permutations of a given charset.
"""

from __future__ import print_function

from itertools import product
from collections import OrderedDict

from ._util import (parse_charset,
                    scan_pattern)


class Generator(object):
    """
    Wordlist class is the wordlist itself, will do the job
    """
    def __init__(self, charset, delimiter=''):
        self.charset = parse_charset(charset)
        self.delimiter = delimiter

    def generate(self, minlen, maxlen):
        """
        Generates words of different length without storing
        them into memory, enforced by itertools.product
        """
        if minlen < 1 or maxlen < minlen:
            raise ValueError()

        for cur in range(minlen, maxlen + 1):
            # string product generator
            str_generator = product(self.charset, repeat=cur)
            for each in str_generator:
                # yield the produced word
                yield ''.join(each)+self.delimiter

    def generate_with_pattern(self, pattern=None, data=None, composed='',
                              prev=0):
        """
        Iterative-Recursive algorithm that creates the list
        based on a given pattern
        Each recursive call will concatenate a piece of string
        to the composed parameter
        data contains the dict created by scanning the pattern
        composed contains the current composed word (works recursively)
        prev is the index of the previous data object used.
        """
        if pattern:
            if not prev:
                # the first call should scan the pattern first
                data = scan_pattern(pattern)

            if not data:
                # if the known values in the pattern have been completely
                # used concat the last part, if any, and print it out
                diff = len(pattern)-prev
                if diff and composed:
                    for word in product(self.charset, repeat=diff):
                         # yield the produced word
                        c_word = ''.join(composed) + ''.join(word)
                        yield c_word + self.delimiter

                elif diff:
                    for word in product(self.charset, repeat=diff):
                         # yield the produced word
                        yield ''.join(word) + self.delimiter
                else:
                     # yield the produced word
                    yield ''.join(composed) + self.delimiter
            else:
                # pop a value from the pattern dict concat it to composed
                # concat a new part to the composed string and call this
                # function again with the new composed word
                num, val = data.popitem(last=False)
                for word in product(self.charset, repeat=(num-prev)):
                    tmp_composed = ''.join(composed) + ''.join(word) + val
                    gen = self.generate_with_pattern(pattern=pattern,
                                                     data=OrderedDict(data),
                                                     composed=tmp_composed,
                                                     prev=num+1)
                    for word in gen:
                        yield word
