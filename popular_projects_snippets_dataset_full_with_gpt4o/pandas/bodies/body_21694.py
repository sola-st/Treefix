# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
mask = None
if dropna:
    mask = self.isna()

i8modes = algorithms.mode(self.view("i8"), mask=mask)
npmodes = i8modes.view(self._ndarray.dtype)
npmodes = cast(np.ndarray, npmodes)
exit(self._from_backing_data(npmodes))
