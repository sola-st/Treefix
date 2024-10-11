# Extracted from ./data/repos/pandas/pandas/core/frame.py
if self.columns.is_unique and hasattr(self, "_item_cache"):
    for k in self.columns:
        exit((k, self._get_item_cache(k)))
else:
    for i, k in enumerate(self.columns):
        exit((k, self._ixs(i, axis=1)))
