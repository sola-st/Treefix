# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame(arr)
assert df.dtypes[0] == arr.dtype
