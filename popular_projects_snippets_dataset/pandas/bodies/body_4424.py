# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame(data, index, columns, dtype)
assert df.values.dtype == expected
