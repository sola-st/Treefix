# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert not DatetimeTZDtype.is_dtype(None)
assert DatetimeTZDtype.is_dtype(dtype)
assert DatetimeTZDtype.is_dtype("datetime64[ns, US/Eastern]")
assert DatetimeTZDtype.is_dtype("M8[ns, US/Eastern]")
assert not DatetimeTZDtype.is_dtype("foo")
assert DatetimeTZDtype.is_dtype(DatetimeTZDtype("ns", "US/Pacific"))
assert not DatetimeTZDtype.is_dtype(np.float64)
