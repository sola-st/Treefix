# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# see gh-13583
x = [
    Timestamp("2011-01-01", tz=dateutil.tz.tzlocal()),
    Timestamp("2011-02-01", tz=dateutil.tz.tzlocal()),
]
y = [
    Timestamp("2012-01-01", tz=dateutil.tz.tzlocal()),
    Timestamp("2012-02-01", tz=dateutil.tz.tzlocal()),
]

result = concat([Series(x), Series(y)], ignore_index=True)
tm.assert_series_equal(result, Series(x + y))
assert result.dtype == "datetime64[ns, tzlocal()]"
