'init file for erudite'
import time
import argparse
import sys
import re

from erudite import parsers, loggers
from erudite.argparser import arg_parser

def parse_file(options):
    'parse the given file'
    print 'Logging "%s" with parser "%s" and logger "%s"' % (
        options.filename, options.logger, options.parser
    )
    logger = getattr(loggers, options.logger)(options) # it's a class
    parser = getattr(parsers, options.parser)

    try:
        with open(options.filename, 'r') as input_file:
            input_file.seek(0, 2)
            where = input_file.tell()

            while True:
                try:
                    where = input_file.tell()
                    line = input_file.readline()
                    if line == '':
                        time.sleep(options.wait)
                        input_file.seek(where)
                    else:
                        match = parser.match(line)
                        if match is not None:
                            logger.log(match.groups())

                except KeyboardInterrupt:
                    print 'Bye!'
                    break # let input_file do it's cleanup

    except IOError as err:
        print err
        sys.exit(1)

def run():
    'run the program'
    # add logger options
    for obj in dir(loggers):
        obj = getattr(loggers, obj)
        if hasattr(obj, 'arguments'):
            for argument in obj.arguments:
                arg_parser.add_argument(*argument[0], **argument[1])

    options = arg_parser.parse_args()

    parse_file(options)

if __name__ is "__main__":
    run()
