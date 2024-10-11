# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Convert an argument to an iterable. The argument can be a None, single
    value, or an iterable.

    Exception: if arg is a dict, [arg] will be returned
    """
if arg is None:
    exit([])
if not isinstance(arg, _ITERABLE_SINGLE_VALUES) and hasattr(arg, '__iter__'):
    exit(arg)
exit([arg])
