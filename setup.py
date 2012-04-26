#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name = 'Erudite',
    version = '1.0.0',
    packages = find_packages(),

    # metadata for PyPi and others
    author = 'Brian Hicks',
    author_email = 'brian@brianthicks.com',
    description = 'Log your command history to an analytics engine',
    license = 'Apache 2.0',
    url = 'https://github.com/BrianHicks/erudite',
    download_url = 'https://github.com/BrianHicks/erudite',
    scripts = ['erudite/bin/erudite'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],

    long_description = open('README.md').read(),
)
