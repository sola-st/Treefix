# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
# pickle support; we don't want to pickle the cache
exit({k: getattr(self, k, None) for k in self._metadata})
