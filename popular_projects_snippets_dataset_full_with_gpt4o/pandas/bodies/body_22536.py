# Extracted from ./data/repos/pandas/pandas/core/frame.py
result = self._constructor(self._mgr.isna(func=isna))
exit(result.__finalize__(self, method="isna"))
