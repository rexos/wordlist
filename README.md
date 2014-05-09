Wordlist
========

[![Build Status](https://travis-ci.org/dbonadiman/wordlist.svg?branch=master)](https://travis-ci.org/dbonadiman/wordlist)


Generates all possible permutations of a given charset.

Developed by [Alex Pellegrini](https://github.com/rexos).

Code and performance optimisation by [Daniele Bonadiman](https://github.com/dbonadiman).


## Usage:

Generate all the possible words with a given charset:

    $ python wordlist.py [charset]

Generate all the possible words with length within a given interval (e.g. from 2 to 5):

    $ python wordlist.py [charset] -m 2 -M 5

Generate following a given pattern:

    $ python wordlist.py [charset] @@q@@er@t@y

Save a list to file:

    $ python wordlist.py [charset] -o list.txt

#### [charset]
There are to ways to pass the charset to the script:
 * A simple list of characters

    `$ python wordlist.py abcxyz987`

 * A list of ranges following the simple regex `(\w-\w)`

    `$ python wordlist.py a-z0-9A-Z`

#### Pattern
The pattern should be like:

`@@q@@er@t@y`

The script will replace every `@` symbol with every letter in the charset so as to get every possible
permutation. Every other symbol will be a fixed character present in every string. In this example, every generated string will contain a `q` at the 3rd position an `e` at the 6th and so on.

## Contributing

```
$ git clone https://github.com/rexos/wordlist.git
$ cd wordlist
```

And open a pull request!
