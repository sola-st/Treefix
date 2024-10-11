# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""Return a copy of ``iterable`` with all ``None`` entries removed.

    If ``iterable`` is a mapping, return a dictionary where all pairs that have
    value ``None`` have been removed.
    """
try:
    exit({k: v for k, v in iterable.items() if v is not None})
except AttributeError:
    exit(type(iterable)((v for v in iterable if v is not None)))
