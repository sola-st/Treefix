# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH24386: Ensure dtypes are set correctly for an empty DataFrame.
# Empty DataFrame is generated via dictionary data with non-overlapping columns.
data = DataFrame({"a": [1, 2]}, columns=["b"], dtype=dtype)

assert data.b.dtype == dtype
