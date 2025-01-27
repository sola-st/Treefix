# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame({0: arr})
assert df.dtypes[0] == arr.dtype
