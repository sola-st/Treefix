# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series
obj = klass([1.1, np.nan, 3.3, 4.4])
assert obj.dtype == np.float64

exp = klass([1.1, fill_val, 3.3, 4.4])
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
