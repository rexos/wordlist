Wordlist
========


Generates all possible permutations of a given charset.

Developed by [Alex Pellegrini](https://github.com/rexos).

Code and performance optimisation by [Daniele Bonadiman](https://github.com/dbonadiman).


Continuous integration status:

[![Build Status](https://travis-ci.org/dbonadiman/wordlist.svg?branch=master)](https://travis-ci.org/dbonadiman/wordlist)
[![Coverage Status](https://coveralls.io/repos/dbonadiman/wordlist/badge.png?branch=master)](https://coveralls.io/r/dbonadiman/wordlist?branch=master)
[![Requirements Status](https://requires.io/github/dbonadiman/wordlist/requirements.png?branch=master)](https://requires.io/github/dbonadiman/wordlist/requirements/?branch=master)

Pypi status:

[![PyPi version](https://img.shields.io/pypi/v/wordlist.svg)](https://crate.io/packages/wordlist/)
[![PyPi downloads](https://img.shields.io/pypi/dm/wordlist.svg)](https://crate.io/packages/wordlist/)


## Installing:

```
$ pip install wordlist
```

## Usage:

There are two ways to use **_wordlist_** (command line, python)

### Command-line

Generate all the possible words with a given charset:

    $ wordlist [charset]

Generate all the possible words with length within a given interval (e.g. from 2 to 5):

    $ wordlist [charset] -m 2 -M 5

Generate following a given pattern:

    $ wordlist [charset] @@q@@er@t@y

Save a list to file:

    $ wordlist [charset] -o list.txt

or:

    $ wordlist [charset] > list.txt

### Python

Generate all the possible words with length within a given interval (e.g. from 2 to 5):

```python
import wordlist
generator = wordlist.Generator('charset')
for each in generator.generate(2, 5):
    print(each)
```

Generate following a given pattern:

```python
import wordlist
generator = wordlist.Generator('charset')
for each in generator.generate_with_pattern('@@q@@er@t@y'):
    print(each)
```

#### [charset]
There are to ways to pass the charset to the script:
 * A simple list of characters

    `$ wordlist abcxyz987`

 * A list of ranges following the simple regex `(\w-\w)`

    `$ wordlist a-z0-9A-Z`

#### Pattern
The pattern should be like:

`@@q@er@t@y`

The script will replace every `{}` symbol with every letter in the charset so as to get every possible
permutation. Every other symbol will be a fixed character present in every string. In this example, every generated string will contain a `q` at the 3rd position an `e` at the 6th and so on.


## Contributing

```
$ git clone https://github.com/rexos/wordlist.git
$ cd wordlist
$ pip install -r requirements.txt
$ nosetests
```

And open a pull request!
