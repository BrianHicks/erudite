'loggers for erudite'
import sys
try:
    from stathat import StatHat
except ImportError:
    StatHat = None

class NoOpLogger(object):
    'Base Logger Object, does not log anything'
    arguments = []
    def __init__(self, options):
        'initialize this object with the options'
        pass

    def log(self, values):
        'log a value'
        pass


class PrintingLogger(NoOpLogger):
    'Printing logger'
    options = []
    def log(self, values):
        'print the values'
        print ', '.join(values)


class StatHatLogger(NoOpLogger):
    'stathat.com logger'
    arguments = [
        (
            ['--stathat-key'],
            dict(type=None, help="Key to use for StatHat (only required if using StatHatLogger"),
        ),
        (
            ['--stathat-prefix'],
            dict(type=str, help="Prefix for stathat stats"),
        ),
    ]

    def __init__(self, options):
        'initialize this logger'
        super(StatHatLogger, self).__init__(options)

        # stathat library is required
        if StatHat is None:
            print 'stathat module is required for this logger'
            sys.exit(3)

        if options.stathat_key is None:
            print 'stathat-key is a required argument when using the stathat logger'
            sys.exit(2)

        self.stathat = StatHat(options.stathat_key)
        print 'Initialized stathat for %s' % options.stathat_key

        if options.stathat_prefix is not None:
            self.prefix = '%s.' % options.stathat_prefix
            print '\t... with prefix %s' % options.stathat_prefix
        else:
            self.prefix = ''
            print '\t... with no prefix'


    def log(self, values):
        'send a stat off to stathat'
        if len(values) > 1:
            print 'stathat logger can only use parsers with single arguments'
            sys.exit(2)

        key = self.prefix + values[0]
        result = self.stathat.count(key, 1)
        print 'Logging "%s". Result: %s' % (key, result)
