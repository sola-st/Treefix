# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# gh-11755: tz and no tz
x = Series(date_range("20151124 08:00", "20151124 09:00", freq="1h", tz="UTC"))
y = Series(date_range("2012-01-01", "2012-01-02"))
expected = Series([x[0], x[1], y[0], y[1]], dtype="object")
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)

# gh-11887: concat tz and object
x = Series(date_range("20151124 08:00", "20151124 09:00", freq="1h", tz="UTC"))
y = Series(["a", "b"])
expected = Series([x[0], x[1], y[0], y[1]], dtype="object")
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)

# see gh-12217 and gh-12306
# Concatenating two UTC times
first = DataFrame([[datetime(2016, 1, 1)]])
first[0] = first[0].dt.tz_localize("UTC")

second = DataFrame([[datetime(2016, 1, 2)]])
second[0] = second[0].dt.tz_localize("UTC")

result = concat([first, second])
assert result[0].dtype == "datetime64[ns, UTC]"

# Concatenating two London times
first = DataFrame([[datetime(2016, 1, 1)]])
first[0] = first[0].dt.tz_localize("Europe/London")

second = DataFrame([[datetime(2016, 1, 2)]])
second[0] = second[0].dt.tz_localize("Europe/London")

result = concat([first, second])
assert result[0].dtype == "datetime64[ns, Europe/London]"

# Concatenating 2+1 London times
first = DataFrame([[datetime(2016, 1, 1)], [datetime(2016, 1, 2)]])
first[0] = first[0].dt.tz_localize("Europe/London")

second = DataFrame([[datetime(2016, 1, 3)]])
second[0] = second[0].dt.tz_localize("Europe/London")

result = concat([first, second])
assert result[0].dtype == "datetime64[ns, Europe/London]"

# Concat'ing 1+2 London times
first = DataFrame([[datetime(2016, 1, 1)]])
first[0] = first[0].dt.tz_localize("Europe/London")

second = DataFrame([[datetime(2016, 1, 2)], [datetime(2016, 1, 3)]])
second[0] = second[0].dt.tz_localize("Europe/London")

result = concat([first, second])
assert result[0].dtype == "datetime64[ns, Europe/London]"
