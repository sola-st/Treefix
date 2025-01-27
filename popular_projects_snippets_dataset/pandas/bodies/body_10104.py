# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH 7898
A = Series(np.random.randn(50), index=range(50))
B = A[2:] + np.random.randn(48)

A[:10] = np.NaN
B.iloc[-10:] = np.NaN

result = getattr(A.ewm(com=20, min_periods=min_periods), name)(B)
# binary functions (ewmcov, ewmcorr) with bias=False require at
# least two values
assert np.isnan(result.values[:11]).all()
assert not np.isnan(result.values[11:]).any()

# check series of length 0
empty = Series([], dtype=np.float64)
result = getattr(empty.ewm(com=50, min_periods=min_periods), name)(empty)
tm.assert_series_equal(result, empty)

# check series of length 1
result = getattr(Series([1.0]).ewm(com=50, min_periods=min_periods), name)(
    Series([1.0])
)
tm.assert_series_equal(result, Series([np.NaN]))
