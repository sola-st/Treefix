# Extracted from ./data/repos/pandas/pandas/core/series.py
loc = self.index.get_loc(key)

# this is equivalent to self._values[key] = value
self._mgr.setitem_inplace(loc, value)
