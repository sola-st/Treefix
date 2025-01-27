# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
ii = pd.interval_range(1.0, 5.0, closed="right").insert(1, np.nan)
assert isinstance(ii.dtype, pd.IntervalDtype)
obj = index_or_series(ii)

exp = index_or_series([ii[0], fill_val, ii[2], ii[3], ii[4]], dtype=object)

fill_dtype = object
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
