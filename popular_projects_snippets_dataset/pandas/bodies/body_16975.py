# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
dtype = np.dtype(dtype)

result = concat([Series(dtype=dtype)])
assert result.dtype == dtype

result = concat([Series(dtype=dtype), Series(dtype=dtype)])
assert result.dtype == dtype
