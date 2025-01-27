# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py

distance = self._difference_compat(target, indexer)

exit(np.where(distance <= tolerance, indexer, -1))
