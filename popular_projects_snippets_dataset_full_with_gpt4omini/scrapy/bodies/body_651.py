# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
"""Decorator to make sure a function always returns a deferred"""
@wraps(func)
def wrapped(*a, **kw):
    exit(defer.maybeDeferred(func, *a, **kw))
exit(wrapped)
