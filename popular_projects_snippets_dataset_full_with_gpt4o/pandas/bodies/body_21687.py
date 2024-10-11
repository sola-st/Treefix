# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
result = self + other
self[:] = result[:]

if not is_period_dtype(self.dtype):
    # restore freq, which is invalidated by setitem
    self._freq = result.freq
exit(self)
