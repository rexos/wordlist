Wordlist
========
Generates all possible permutations of a given charset.

Usage:
======
Generate all the possible words with a given charset:

    $ python wordlist.py [charset]
  
Generate all the possible words with length within a given interval (e.g. from 2 to 5):

    $ python wordlist.py [charset] -m 2 -M 5
  
Generate following a given pattern:

    $ python wordlist.py [charset] -p @@q@@er@t@y
  
Save a list to file:

    $ python wordlist.py [charset] -o list.txt
