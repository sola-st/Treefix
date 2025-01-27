# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/app.py
"""Runs the program with an optional 'main' function and 'argv' list."""

main = main or _sys.modules['__main__'].main

_run(main=main, argv=argv, flags_parser=_parse_flags_tolerate_undef)
