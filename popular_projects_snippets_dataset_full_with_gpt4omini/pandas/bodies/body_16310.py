# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH3416
pydates = [datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3)]
dates = [np.datetime64(x) for x in pydates]

ser = Series(dates)
assert ser.dtype == "M8[ns]"

ser.iloc[0] = np.nan
assert ser.dtype == "M8[ns]"

# GH3414 related
expected = Series(pydates, dtype="datetime64[ms]")

result = Series(Series(dates).view(np.int64) / 1000000, dtype="M8[ms]")
tm.assert_series_equal(result, expected)

result = Series(dates, dtype="datetime64[ms]")
tm.assert_series_equal(result, expected)

expected = Series(
    [NaT, datetime(2013, 1, 2), datetime(2013, 1, 3)], dtype="datetime64[ns]"
)
result = Series([np.nan] + dates[1:], dtype="datetime64[ns]")
tm.assert_series_equal(result, expected)
