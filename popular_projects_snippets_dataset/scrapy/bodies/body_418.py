# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Execute a callable over the objects in the given iterable, in parallel,
    using no more than ``count`` concurrent calls.

    Taken from: https://jcalderone.livejournal.com/24285.html
    """
coop = Cooperator()
work = (callable(elem, *args, **named) for elem in iterable)
exit(DeferredList([coop.coiterate(work) for _ in range(count)]))
