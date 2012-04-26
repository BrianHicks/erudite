'''
------------------------------------------------------------------------------
Parse log files for analytics purposes

Exit codes:
 - 0: all good
 - 1: general error
 - 2: bad option
 - 3: missing requirement

Not all requirements are installed by default (for example, the stathat module
for StatHatLogger).
------------------------------------------------------------------------------
'''
import argparse
from erudite import parsers, loggers

arg_parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# get parser regular expressions - in a duck typey way
parser_names = [
    parser for parser in dir(parsers)
    if hasattr(getattr(parsers, parser), 'match') and parser is not 're'
]
arg_parser.add_argument(
    '-p', '--parser', type=str,
    help='Parser to use.', choices=parser_names,
    default='zsh_history'
)

# get logger names - anything that subclasses logger.NoOpLogger
noop = loggers.NoOpLogger
logger_names = [
    logger for logger in dir(loggers)
    if getattr(loggers, logger) is noop or getattr(loggers, logger) in noop.__subclasses__()
]
arg_parser.add_argument(
    '-l', '--logger', type=str,
    help='Logger to use.', choices=logger_names,
    default='StatHatLogger'
)

arg_parser.add_argument('-w', '--wait', type=float, default=1.0, help='Time to wait between scans')
arg_parser.add_argument('filename', type=str, help='File to tail and parse')
