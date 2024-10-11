# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
assert not isinstance(other, Tick)

self._require_matching_freq(other, base=True)
exit(self._addsub_int_array_or_scalar(other.n, operator.add))
