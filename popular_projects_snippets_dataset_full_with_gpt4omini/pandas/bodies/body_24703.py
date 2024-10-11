# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
if inherited is not None:
    self.inherited = self.compute_css(inherited)
else:
    self.inherited = None
# We should avoid lru_cache on the __call__ method.
# Otherwise once the method __call__ has been called
# garbage collection no longer deletes the instance.
self._call_cached = lru_cache(maxsize=None)(self._call_uncached)
