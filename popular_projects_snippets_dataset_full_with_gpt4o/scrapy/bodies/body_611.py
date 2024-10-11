# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""Decorator to cache the result of a method (without arguments) using a
    weak reference to its object
    """
cache = weakref.WeakKeyDictionary()

@wraps(method)
def new_method(self, *args, **kwargs):
    if self not in cache:
        cache[self] = method(self, *args, **kwargs)
    exit(cache[self])

exit(new_method)
