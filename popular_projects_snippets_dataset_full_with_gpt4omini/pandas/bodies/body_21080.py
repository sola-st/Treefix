# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
arr = self._ndarray.copy()
mask = self.isna()
arr[mask] = None
exit((arr, None))
