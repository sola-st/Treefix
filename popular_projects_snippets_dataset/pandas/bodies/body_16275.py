# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
ser = Series([1, 2, 3], dtype="category")
assert is_categorical_dtype(ser)
assert is_categorical_dtype(ser.dtype)
