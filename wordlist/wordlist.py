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

from ._util import (parse_charset,
                    get_pattern_length)


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

    def generate_with_pattern(self, pattern=None):
        """
        Algorithm that creates the list
        based on a given pattern
        The pattern must be like string format patter:
        e.g: a{}b will match an 'a' follow by any character follow by a 'b'

        To scape the curly brackets just use {{}}
        """

        curlen = get_pattern_length(pattern)
        str_generator = product(self.charset, repeat=curlen)
        for each in str_generator:
            yield pattern.format(*each)+self.delimiter
