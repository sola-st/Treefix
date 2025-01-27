# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_period_dtype(dtype)

pidx = pd.period_range("2013-01-01 09:00", periods=5, freq="H")

assert is_period_dtype(pidx.dtype)
assert is_period_dtype(pidx)

s = Series(pidx, name="A")

assert is_period_dtype(s.dtype)
assert is_period_dtype(s)

assert not is_period_dtype(np.dtype("float64"))
assert not is_period_dtype(1.0)
