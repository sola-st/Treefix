# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py

assert is_categorical_dtype(dtype)

factor = Categorical(["a", "b", "b", "a", "a", "c", "c", "c"])

s = Series(factor, name="A")

# dtypes
assert is_categorical_dtype(s.dtype)
assert is_categorical_dtype(s)
assert not is_categorical_dtype(np.dtype("float64"))
