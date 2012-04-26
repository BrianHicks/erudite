#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name = 'Erudite',
    version = '0.0.1',
    packages = find_packages(),

    install_requires = [
        'pyyaml',
    ],

    # metadata for PyPi and others
    author = 'Brian Hicks',
    author_email = 'brian@brianthicks.com',
    description = 'Log your command history to an analytics engine',
    license = 'TODO',
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
