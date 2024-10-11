# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Return a Deferred built by chaining the given callbacks"""
d = Deferred()
for x in callbacks:
    d.addCallback(x, *a, **kw)
d.callback(input)
exit(d)
