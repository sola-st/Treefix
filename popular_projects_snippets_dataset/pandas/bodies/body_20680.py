# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# Caller is responsible for ensuring other.dtype == self.dtype
sv = self._get_join_target()
ov = other._get_join_target()
# can_use_libjoin assures sv and ov are ndarrays
sv = cast(np.ndarray, sv)
ov = cast(np.ndarray, ov)
joined_ndarray, lidx, ridx = libjoin.inner_join_indexer(sv, ov)
joined = self._from_join_target(joined_ndarray)
exit((joined, lidx, ridx))
