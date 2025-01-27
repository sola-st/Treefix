# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series
obj = klass([1 + 1j, np.nan, 3 + 3j, 4 + 4j], dtype=np.complex128)
assert obj.dtype == np.complex128

exp = klass([1 + 1j, fill_val, 3 + 3j, 4 + 4j])
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
