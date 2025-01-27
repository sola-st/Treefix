# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_float_dtype(str)
assert not com.is_float_dtype(int)
assert not com.is_float_dtype(pd.Series([1, 2]))
assert not com.is_float_dtype(np.array(["a", "b"]))

assert com.is_float_dtype(float)
assert com.is_float_dtype(pd.Index([1, 2.0]))
