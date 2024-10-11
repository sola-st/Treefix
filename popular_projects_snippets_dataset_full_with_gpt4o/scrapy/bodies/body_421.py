# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
# This gets called on any exceptions in aiterator.__anext__().
# It handles StopAsyncIteration by stopping the iteration and reraises all others.
self.anext_deferred = None
failure.trap(StopAsyncIteration)
self.finished = True
for d in self.waiting_deferreds:
    d.callback(None)
