# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH-20865
result = Series(dtype=dtype, index=index)
assert result.dtype == dtype
assert len(result) == 0
