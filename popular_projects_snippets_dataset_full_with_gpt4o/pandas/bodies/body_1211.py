# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
obj = pd.Index(list("abcd"))
assert obj.dtype == object

exp = pd.Index(["a", coerced_val, "b", "c", "d"])
self._assert_insert_conversion(obj, insert, exp, coerced_dtype)
