# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Same as twisted.internet.defer.fail but delay calling errback until
    next reactor loop

    It delays by 100ms so reactor has a chance to go through readers and writers
    before attending pending delayed calls, so do not set delay to zero.
    """
from twisted.internet import reactor
d = Deferred()
reactor.callLater(0.1, d.errback, _failure)
exit(d)
