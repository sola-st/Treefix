# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
tz = "US/Central"
data = DatetimeArray(pd.date_range("2017", periods=2, tz=tz))
result = np.asarray(data)

expected = np.array(
    [
        pd.Timestamp("2017-01-01T00:00:00", tz=tz),
        pd.Timestamp("2017-01-02T00:00:00", tz=tz),
    ],
    dtype=object,
)
tm.assert_numpy_array_equal(result, expected)

result = np.asarray(data, dtype=object)
tm.assert_numpy_array_equal(result, expected)

result = np.asarray(data, dtype="M8[ns]")

expected = np.array(
    ["2017-01-01T06:00:00", "2017-01-02T06:00:00"], dtype="M8[ns]"
)
tm.assert_numpy_array_equal(result, expected)
