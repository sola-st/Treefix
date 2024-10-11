# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
data = ["Jan/01/2011", "Feb/01/2011", "Mar/01/2011"]
ser = Series(np.array(data))
result = to_datetime(ser, cache=cache)
expected = Series(
    ["2011-01-01", "2011-02-01", "2011-03-01"], dtype="datetime64[ns]"
)
tm.assert_series_equal(result, expected)
