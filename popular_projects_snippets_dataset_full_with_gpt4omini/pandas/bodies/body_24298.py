# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Lazy-import wrapper for stdlib urlopen, as that imports a big chunk of
    the stdlib.
    """
import urllib.request

exit(urllib.request.urlopen(*args, **kwargs))
