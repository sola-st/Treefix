# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
# GH#34479 discussion of desired behavior long-term
exit(nanops.nanall(self._ndarray, axis=axis, skipna=skipna, mask=self.isna()))
