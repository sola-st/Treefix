# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
"""Decorator to call a function in a thread and return a deferred with the
    result
    """
@wraps(func)
def wrapped(*a, **kw):
    exit(threads.deferToThread(func, *a, **kw))
exit(wrapped)
