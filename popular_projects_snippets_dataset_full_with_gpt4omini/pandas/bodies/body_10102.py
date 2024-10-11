# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# excluding NaNs correctly
arr = np.random.randn(50)
arr[:10] = np.NaN
arr[-10:] = np.NaN
s = Series(arr)

# check min_periods
# GH 7898
result = getattr(s.ewm(com=50, min_periods=2), name)()
assert result[:11].isna().all()
assert not result[11:].isna().any()

result = getattr(s.ewm(com=50, min_periods=min_periods), name)()
if name == "mean":
    assert result[:10].isna().all()
    assert not result[10:].isna().any()
else:
    # ewm.std, ewm.var (with bias=False) require at least
    # two values
    assert result[:11].isna().all()
    assert not result[11:].isna().any()

# check series of length 0
result = getattr(Series(dtype=object).ewm(com=50, min_periods=min_periods), name)()
tm.assert_series_equal(result, Series(dtype="float64"))

# check series of length 1
result = getattr(Series([1.0]).ewm(50, min_periods=min_periods), name)()
if name == "mean":
    tm.assert_series_equal(result, Series([1.0]))
else:
    # ewm.std, ewm.var with bias=False require at least
    # two values
    tm.assert_series_equal(result, Series([np.NaN]))

# pass in ints
result2 = getattr(Series(np.arange(50)).ewm(span=10), name)()
assert result2.dtype == np.float_
