# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH21358
tz = timezones.maybe_get_tz(tz_naive_fixture)

expected = np.array([time(10, 20, 30, tzinfo=tz), pd.NaT])

index = DatetimeIndex(["2018-06-04 10:20:30", pd.NaT], tz=tz)
result = index.timetz

tm.assert_numpy_array_equal(result, expected)
