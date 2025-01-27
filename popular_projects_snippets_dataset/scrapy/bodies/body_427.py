# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Return a Deferred with the output of all successful calls to the given
    callbacks
    """
dfds = [defer.succeed(input).addCallback(x, *a, **kw) for x in callbacks]
d = DeferredList(dfds, fireOnOneErrback=True, consumeErrors=True)
d.addCallbacks(lambda r: [x[1] for x in r], lambda f: f.value.subFailure)
exit(d)
