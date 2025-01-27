# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series
obj = klass(["a", np.nan, "c", "d"])
assert obj.dtype == object

exp = klass(["a", fill_val, "c", "d"])
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
