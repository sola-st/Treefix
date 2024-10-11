# Extracted from ./data/repos/pandas/pandas/core/series.py
if isinstance(key, (Index, Series)):
    key = key._values

self._mgr = self._mgr.setitem(indexer=key, value=value)
self._maybe_update_cacher()
