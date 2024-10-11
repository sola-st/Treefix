# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
s = Series([0] * 2 + [np.nan] * 2, index=date_range("2017", periods=4))
result = methodcaller(method, **method_args)(s.resample("2d"))
expected = Series(
    [0.0, unit], index=pd.DatetimeIndex(["2017-01-01", "2017-01-03"], freq="2D")
)
tm.assert_series_equal(result, expected)
