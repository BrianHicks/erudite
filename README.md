ERUDITE
=======

Tail files, and do things with them.

Installation
------------

Run `pip install erudite` or if it's your thing: `easy_install erudite`. You'll
need to also get argparse if you're using a Python less than 2.7.

This might work on Python 3+, but I haven't tested it.

Examples
--------

Send first words of your zsh history to [StatHat](http://www.stathat.com)
(currently the default):

    erudite --parser=zsh_history --logger=StatHatLogger --stathat-key=test@example.com ~/.zsh_history

If you just want to play around, and see what you can do:

    erudite --parser=zsh_history --logger=PrintingLogger ~/.zsh_history

Developing
----------

Parsers (used to parse lines) are in `erudite/parsers.py`, and loggers (used to
do things with parsed lines) are in `erudite/loggers.py`.

Contributing
------------

It would be totally awesome to have many many more options in this script. I'm
totally open to contributions. But there are a few things that will help me:

 - Your fork should have a topic branch with your feature, requesting to pull
   against `develop`
 - Please don't add any requirements for loggers to setup.py - catch
   ImportError and exit gracefully. (see StatHatLogger for an example)
 - If you're adding a parser, it would be awesome if you could attach some
   sample input.
 - Just for fun, you might want to run pylint against your changes.
 - If you're changing default settings, it's totally cool. Just ask me first.
 - You should add yourself to Authors in the README.

In particular, here are some things/ideas that would be great to have:

 - Parser for [bash](http://www.gnu.org/software/bash/) history
 - Parser for database logs
 - Logger for [redis][1]/[mongo][2]/whatever nosql store you want to use
 - Logger for [StatsD](https://github.com/etsy/statsd)
 - And if you're feeling particularly ambitious: tests

[1]: http://redis.io/
[2]: http://www.mongodb.org/

Authors
-------

 - Brian Hicks

License
-------

See LICENSE.md (hint: it's Apache 2.0)
