'parsers for various inputs'
# these are regexes, which returns one (or more, if the logger is implemented for
# it) group
import re

zsh_history = re.compile(r':\s\d+:\d;(\w*).*')
zsh_history_full = re.compile(r':\s\d+:\d;(.*)')
