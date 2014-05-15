try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import wordlist

install_requires = []


config = {
    'description': 'Wordlist generator, creates dictionaries of words',
    'author': 'Rexos',
    'url': 'https://github.com/rexos/wordlist',
    'download_url': 'https://github.com/rexos/wordlist/tarball/1.0',
    'author_email': 'alex.pellegrini@live.com',
    'version': wordlist.__version__,
    'install_requires': install_requires,
    'packages': ['wordlist'],
    'scripts': ['bin/wordlist'],
    'keywords': ['words', 'generator', 'wordlist'],
    'name': wordlist.__title__
}

setup(**config)


#TODO: change the download_url
#TODO: change author author_email
