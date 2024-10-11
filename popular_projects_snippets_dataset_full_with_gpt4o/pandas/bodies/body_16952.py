# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# see gh-12620: tz and timedelta
x = [
    Timestamp("2011-01-01", tz="US/Eastern"),
    Timestamp("2011-02-01", tz="US/Eastern"),
]
y = [pd.Timedelta("1 day"), pd.Timedelta("2 day")]
result = concat([Series(x), Series(y)], ignore_index=True)
tm.assert_series_equal(result, Series(x + y, dtype="object"))

# tz and period
y = [pd.Period("2011-03", freq="M"), pd.Period("2011-04", freq="M")]
result = concat([Series(x), Series(y)], ignore_index=True)
tm.assert_series_equal(result, Series(x + y, dtype="object"))
