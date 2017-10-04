# -*- coding: utf-8 -*-
"""Wordlist

Generates all possible permutations of a given charset.

Usage:
>>>import wordlist
>>>generator = wordlist.Generator('ab')
>>>for each in generator.generate(1, 2):
...    print(each)
a
b
aa
ab
ba
bb

>>>import wordlist
>>>generator = wordlist.Generator('ab')
>>>for each in generator.generate_with_pattern('@a'):
...    print(each)
aa
ba
"""
from .wordlist import Generator

__title__ = "wordlist"
__version__ = '1.0.3'
__all__ = ["Generator"]
