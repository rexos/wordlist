
############################################
#                                          #
# Wordlist generator, creates dictionaries #
# Developed by rexos.                      #
# Code and performance optimisation by     #
# dbonadiman.                              #
#                                          #
############################################
from __future__ import print_function

import sys
import os

from collections import OrderedDict

from ._util import (str_product,
                    parse_charset,
                    progress,
                    scan_pattern)


class Generator(object):
    """
    Wordlist class is the wordlist itself, will do the job
    """
    def __init__(self, charset, minlen, maxlen, pattern, filedesc,
                 verbose=False):

        self.charset = parse_charset(charset)
        self.min = minlen
        self.max = maxlen
        self.verbose = verbose
        self.pattern = pattern
        self.filedesc = filedesc
        self.size = self.__total()

    def generate(self):
        """
        Generates words of different length without storing
        them into memory, enforced by itertools.product
        """

        counter = 0
        for cur in range(self.min, self.max + 1):
            # string product generator
            str_generator = str_product(self.charset, cur, '\n')
            # append the generated words to the file
            self.filedesc.writelines(str_generator)
            # a progress bar to stdout
            if self.verbose and self.filedesc != sys.stdout:
                counter += len(self.charset) ** cur
                progress(counter, self.size)
        # once the work is done tell the kernel to point
        # the file pointer to the end of the file so as
        # to be able to get the file size.
        if self.filedesc != sys.stdout:
            self.filedesc.seek(0, os.SEEK_END)
            print('\n' + __file__ + ' List size: ' +
                  str(self.filedesc.tell()) + ' bytes')
            self.filedesc.close()

    def generate_with_pattern(self, data=None, composed='', prev=0):
        """
        Iterative-Recursive algorithm that creates the list
        based on a given pattern
        Each recursive call will concatenate a piece of string
        to the composed parameter
        data contains the dict created by scanning the pattern
        composed contains the current composed word (works recursively)
        prev is the index of the previous data object used.
        """

        if not prev:
            # the first call should scan the pattern first
            data = scan_pattern(self.pattern)

        if not data:
            # if the known values in the pattern have been completely
            # used concat the last part, if any, and print it out
            diff = len(self.pattern)-prev
            if diff:
                for word in str_product(self.charset, diff):
                    print(composed + word, file=self.filedesc)
            else:
                # the word is complete, print it out to file or stdout
                print(composed, file=self.filedesc)
        else:
            # pop a value from the pattern dict concat it to composed
            # concat a new part to the composed string and call this
            # function again with the new composed word
            num, val = data.popitem(last=False)
            for word in str_product(self.charset, num - prev):
                self.generate_with_pattern(OrderedDict(data), composed +
                                           word + val, num+1)

    def __total(self):
        """
        Computes the number of words to be generated.
        It will be used to prompt a progress bar.
        """
        ary = range(self.min, self.max + 1)
        length = len(self.charset)
        return sum(pow(length, x) for x in ary)
