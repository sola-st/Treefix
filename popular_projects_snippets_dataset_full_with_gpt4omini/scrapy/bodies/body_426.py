# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Return a Deferred built by chaining the given callbacks and errbacks"""
d = Deferred()
for cb, eb in zip(callbacks, errbacks):
    d.addCallbacks(
        callback=cb, errback=eb,
        callbackArgs=a, callbackKeywords=kw,
        errbackArgs=a, errbackKeywords=kw,
    )
if isinstance(input, failure.Failure):
    d.errback(input)
else:
    d.callback(input)
exit(d)
