""".util
is a private module containing utility
used for the actual implementation of
the wordlist generator
"""

from collections import OrderedDict


def char_range(starting_char, ending_char):
    """
    Create a range generator for chars
    """
    assert isinstance(starting_char, str), 'char_range: Wrong argument/s type'
    assert isinstance(ending_char, str), 'char_range: Wrong argument/s type'

    for char in range(ord(starting_char), ord(ending_char) + 1):
        yield chr(char)


def parse_charset(charset):
    """
    Finds out whether there are intervals to expand and
    creates the charset
    """
    import re
    regex = r'(\w-\w)'
    pat = re.compile(regex)
    found = pat.findall(charset)
    result = ''
    if found:
        for element in found:
            for char in char_range(element[0], element[-1]):
                result += char
        return result
    return charset


def scan_pattern(string):
    """
    Scans the pattern in the form @@@a@@ returning an OrderedDict
    containing the position of the fixed characters.
    """
    res = OrderedDict([(i, x) for i, x in enumerate(string) if x != '@'])
    return res
