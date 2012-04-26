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

Contributing
------------

Parsers (used to parse lines) are in `erudite/parsers.py`, and loggers (used to
do things with parsed lines) are in `erudite/loggers.py`.

Create a topic branch with your feature, and create a pull request. I'll
probably accept it. Please update the readme, but don't add any install
requirements in `setup.py`. Catch `ImportErrors` instead, like `StatHatLogger`
does.

Authors
-------

 - Brian Hicks

License
-------

See LICENSE.md (hint: it's Apache 2.0)
