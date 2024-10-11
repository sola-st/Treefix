# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_string_dtype(int)
assert not com.is_string_dtype(pd.Series([1, 2]))

assert com.is_string_dtype(str)
assert com.is_string_dtype(object)
assert com.is_string_dtype(np.array(["a", "b"]))
assert com.is_string_dtype(pd.StringDtype())
