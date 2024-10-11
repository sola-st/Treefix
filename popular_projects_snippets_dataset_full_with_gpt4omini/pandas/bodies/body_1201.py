# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
obj = pd.Series([1, 2, 3, 4])
assert obj.index.dtype == np.int64

exp_index = pd.Index([0, 1, 2, 3, val])
self._assert_setitem_index_conversion(obj, val, exp_index, exp_dtype)
