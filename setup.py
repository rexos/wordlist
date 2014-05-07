try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import wordlist

config = {
    'description': 'Wordlist generator, creates dictionaries of words',
    'author': 'Rexos',
    'url': 'https://github.com/rexos/wordlist',
    'download_url': 'https://github.com/rexos/wordlist/archive/master.zip',
    'author_email': 'etc @ rexos',
    'version': wordlist.__version__,
    'install_requires': [],
    'packages': ['wordlist'],
    'scripts': ['bin/wordlist'],
    'name': wordlist.__title__
}

setup(**config)


#TODO: change the download_url
#TODO: change author author_email
