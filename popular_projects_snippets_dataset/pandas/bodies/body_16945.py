# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 11693
# test for merging NaT series with datetime series.
x = Series(
    date_range("20151124 08:00", "20151124 09:00", freq="1h", tz="US/Eastern")
)
y = Series(pd.NaT, index=[0, 1], dtype="datetime64[ns, US/Eastern]")
expected = Series([x[0], x[1], pd.NaT, pd.NaT])

result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)

# all NaT with tz
expected = Series(pd.NaT, index=range(4), dtype="datetime64[ns, US/Eastern]")
result = concat([y, y], ignore_index=True)
tm.assert_series_equal(result, expected)

# without tz
x = Series(date_range("20151124 08:00", "20151124 09:00", freq="1h"))
y = Series(date_range("20151124 10:00", "20151124 11:00", freq="1h"))
y[:] = pd.NaT
expected = Series([x[0], x[1], pd.NaT, pd.NaT])
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)

# all NaT without tz
x[:] = pd.NaT
expected = Series(pd.NaT, index=range(4), dtype="datetime64[ns]")
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)
