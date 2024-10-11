# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
if dtype is None:
    pytest.skip("np.float128 not available")

ser = Series(range(10), dtype=dtype)
result = getattr(ser, method)()
if is_integer_dtype(dtype) and method not in ["min", "max"]:
    assert result.dtype == np.float64
else:
    assert result.dtype == dtype
