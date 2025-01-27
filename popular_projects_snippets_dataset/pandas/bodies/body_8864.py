# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
data = DatetimeArray(pd.date_range("2017", periods=2))
expected = np.array(
    ["2017-01-01T00:00:00", "2017-01-02T00:00:00"], dtype="datetime64[ns]"
)

result = np.asarray(data)
tm.assert_numpy_array_equal(result, expected)

result = np.asarray(data, dtype=object)
expected = np.array(
    [pd.Timestamp("2017-01-01T00:00:00"), pd.Timestamp("2017-01-02T00:00:00")],
    dtype=object,
)
tm.assert_numpy_array_equal(result, expected)
