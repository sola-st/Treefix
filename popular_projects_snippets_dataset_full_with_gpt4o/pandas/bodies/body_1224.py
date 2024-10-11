# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series

obj = klass([1.1, 2.2, 3.3, 4.4])
assert obj.dtype == np.float64
self._run_test(obj, fill_val, klass, exp_dtype)
