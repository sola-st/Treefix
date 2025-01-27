# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
super().__init__()
self._source_map = converted_fn.ag_source_map
# This may be called repeatedly: once on entry, by the superclass, then by
# each child context manager.
self._cached_map = None
