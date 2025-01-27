# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
mask = self.isna()
if na_value is not lib.no_default and mask.any():
    result = self._ndarray.copy()
    result[mask] = na_value
else:
    result = self._ndarray

result = np.asarray(result, dtype=dtype)

if copy and result is self._ndarray:
    result = result.copy()

exit(result)
