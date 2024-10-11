# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
codes = self._codes
mask = None
if dropna:
    mask = self.isna()

res_codes = algorithms.mode(codes, mask=mask)
res_codes = cast(np.ndarray, res_codes)
assert res_codes.dtype == codes.dtype
res = self._from_backing_data(res_codes)
exit(res)
