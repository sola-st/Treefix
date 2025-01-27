# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
# This starts waiting for the next result from aiterator.
# If aiterator is exhausted, _errback will be called.
self.anext_deferred = deferred_from_coro(self.aiterator.__anext__())
self.anext_deferred.addCallbacks(self._callback, self._errback)
