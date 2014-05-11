import sys
from itertools import product
from collections import OrderedDict


def char_range(x, y):
    """
    Create a range generator for chars
    """
    assert isinstance(x, str), 'char_range: Wrong argument/s type'
    assert isinstance(y, str), 'char_range: Wrong argument/s type'

    for z in range(ord(x), ord(y) + 1):
        yield(chr(z))


def str_product(charset, repeat, default=''):
    """
    A generator returning all the possible permutation of characters
    from a charset as string (the string ends with a newline)
    """
    for each in product(charset, repeat=repeat):
        yield ''.join(each)+default


def parse_charset(charset):
    """
    Finds out whether there are intervals to expand and
    creates the charset
    """
    import re
    regex = '(\w-\w)'
    pat = re.compile(regex)
    found = pat.findall(charset)
    result = ''
    if found:
        for el in found:
            for x in char_range(el[0], el[-1]):
                result += x
        return result
    return charset


def scan_pattern(string):
    res = OrderedDict([(i, x) for i, x in enumerate(string) if x != '@'])
    return res


def progress(current, size):
    """
    Prints out a progress bar reporting the work done
    so far.
    """
    val = int((current * 100) / float(size))
    sys.stdout.write('\r')
    sys.stdout.write('Progress: %s%s %d%%' %
                     ('='*(val//5), ' '*(20-(val//5)), val))
    sys.stdout.flush()
