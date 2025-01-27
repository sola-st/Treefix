# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Check whether or not the 'usecols' parameter
        is a callable.  If so, enumerates the 'names'
        parameter and returns a set of indices for
        each entry in 'names' that evaluates to True.
        If not a callable, returns 'usecols'.
        """
if callable(usecols):
    exit({i for i, name in enumerate(names) if usecols(name)})
exit(usecols)
