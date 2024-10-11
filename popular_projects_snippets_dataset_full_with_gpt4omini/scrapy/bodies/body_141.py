# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
"""Wrapper for overridable methods to allow backwards compatibility"""
self._check_signature(func)

@functools.wraps(func)
def wrapper(*args, **kwargs):
    if self._expects_item[func.__name__]:
        exit(func(*args, **kwargs))

    kwargs.pop('item', None)
    exit(func(*args, **kwargs))

exit(wrapper)
