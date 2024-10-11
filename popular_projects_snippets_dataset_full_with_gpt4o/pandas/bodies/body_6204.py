# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
result = pd.Series(data_missing)
expected = result.copy()
mask = getattr(result, na_func)()
if is_sparse(mask):
    mask = np.array(mask)

mask[:] = True
self.assert_series_equal(result, expected)
