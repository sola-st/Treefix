# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# convert from a numpy array of non-ns timedelta64
arr = np.array([1, 2, 3], dtype="timedelta64[s]")
ser = Series(arr)
assert ser.dtype == arr.dtype

tdi = timedelta_range("00:00:01", periods=3, freq="s").as_unit("s")
expected = Series(tdi)
assert expected.dtype == arr.dtype
tm.assert_series_equal(ser, expected)

# convert from a numpy array of non-ns datetime64
arr = np.array(
    ["2013-01-01", "2013-01-02", "2013-01-03"], dtype="datetime64[D]"
)
ser = Series(arr)
expected = Series(date_range("20130101", periods=3, freq="D"), dtype="M8[s]")
assert expected.dtype == "M8[s]"
tm.assert_series_equal(ser, expected)

arr = np.array(
    ["2013-01-01 00:00:01", "2013-01-01 00:00:02", "2013-01-01 00:00:03"],
    dtype="datetime64[s]",
)
ser = Series(arr)
expected = Series(
    date_range("20130101 00:00:01", periods=3, freq="s"), dtype="M8[s]"
)
assert expected.dtype == "M8[s]"
tm.assert_series_equal(ser, expected)
