# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# Regression test for GH#21230
expected = np.array([date(2018, 6, 4), pd.NaT])

index = DatetimeIndex(["2018-06-04 10:00:00", pd.NaT], dtype=dtype)
result = index.date

tm.assert_numpy_array_equal(result, expected)
