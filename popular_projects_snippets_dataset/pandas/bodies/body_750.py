# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
values = np.arange(10, dtype=np.int32)
result = ensure_int32(values)
assert result.dtype == np.int32

values = np.arange(10, dtype=np.int64)
result = ensure_int32(values)
assert result.dtype == np.int32
