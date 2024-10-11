# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = pd.Series  # TODO: use index_or_series once we have Index[bool]

obj = klass([True, False, True, False])
assert obj.dtype == np.bool_
self._run_test(obj, fill_val, klass, exp_dtype)
