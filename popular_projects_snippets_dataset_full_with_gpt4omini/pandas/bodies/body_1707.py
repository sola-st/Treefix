# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
s = Series(1, index=date_range("2017", periods=2, freq="H"))
resampled = s.resample("30T")
index = pd.DatetimeIndex(
    ["2017-01-01T00:00:00", "2017-01-01T00:30:00", "2017-01-01T01:00:00"],
    freq="30T",
)
result = methodcaller(method, **method_args)(resampled)
expected = Series(expected_values, index=index)
tm.assert_series_equal(result, expected)
