# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
assert other.dtype == self.dtype, (other.dtype, self.dtype)
result = super()._wrap_joined_index(joined, other, lidx, ridx)
result._data._freq = self._get_join_freq(other)
exit(result)
