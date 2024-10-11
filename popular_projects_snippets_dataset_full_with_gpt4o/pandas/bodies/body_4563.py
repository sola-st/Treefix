# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
ser = Series(arr)
assert ser.dtype == arr.dtype
