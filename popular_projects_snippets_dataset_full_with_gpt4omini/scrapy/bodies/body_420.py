# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
# This gets called when the result from aiterator.__anext__() is available.
# It calls the callable on it and sends the result to the oldest waiting Deferred
# (by chaining if the result is a Deferred too or by firing if not).
self.anext_deferred = None
result = self.callable(result, *self.callable_args, **self.callable_kwargs)
d = self.waiting_deferreds.pop(0)
if isinstance(result, Deferred):
    result.chainDeferred(d)
else:
    d.callback(None)
if self.waiting_deferreds:
    self._call_anext()
