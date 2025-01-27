# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# Regression test for GH#21267
expected = np.array([time(10, 20, 30), pd.NaT])

index = DatetimeIndex(["2018-06-04 10:20:30", pd.NaT], dtype=dtype)
result = index.time

tm.assert_numpy_array_equal(result, expected)
