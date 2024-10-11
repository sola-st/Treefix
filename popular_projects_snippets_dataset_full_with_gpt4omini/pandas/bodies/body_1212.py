# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
dtype = any_int_numpy_dtype
obj = pd.Index([1, 2, 3, 4], dtype=dtype)
coerced_dtype = coerced_dtype if coerced_dtype is not None else dtype

exp = pd.Index([1, coerced_val, 2, 3, 4], dtype=coerced_dtype)
self._assert_insert_conversion(obj, insert, exp, coerced_dtype)
