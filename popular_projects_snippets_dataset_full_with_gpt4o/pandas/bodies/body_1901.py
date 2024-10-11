# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 13238
s = Series(
    2, index=date_range("2017-01-01", periods=48, freq="H", tz="US/Eastern")
)
result = s.resample("D").mean()
expected = Series(
    2.0,
    index=pd.DatetimeIndex(
        ["2017-01-01", "2017-01-02"], tz="US/Eastern", freq="D"
    ),
)
tm.assert_series_equal(result, expected)
# Especially assert that the timezone is LMT for pytz
assert result.index.tz == pytz.timezone("US/Eastern")
