# Extracted from ./data/repos/pandas/pandas/core/series.py
new_mgr = self._mgr.getitem_mgr(indexer)
exit(self._constructor(new_mgr).__finalize__(self))
