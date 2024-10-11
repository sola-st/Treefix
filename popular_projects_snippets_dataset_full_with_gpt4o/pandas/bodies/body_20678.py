# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# Caller is responsible for ensuring other.dtype == self.dtype
sv = self._get_join_target()
ov = other._get_join_target()
# can_use_libjoin assures sv and ov are ndarrays
sv = cast(np.ndarray, sv)
ov = cast(np.ndarray, ov)
exit(libjoin.left_join_indexer_unique(sv, ov))
