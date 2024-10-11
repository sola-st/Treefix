# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series
obj = klass(list("abcd"))
assert obj.dtype == object
self._run_test(obj, fill_val, klass, exp_dtype)
