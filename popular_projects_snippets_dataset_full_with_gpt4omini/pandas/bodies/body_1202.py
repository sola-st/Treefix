# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
obj = pd.Series([1, 2, 3, 4], index=[1.1, 2.1, 3.1, 4.1])
assert obj.index.dtype == np.float64

exp_index = pd.Index([1.1, 2.1, 3.1, 4.1, val])
self._assert_setitem_index_conversion(obj, val, exp_index, exp_dtype)
