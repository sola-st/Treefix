# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["a", np.nan, "b", True, datetime.today(), "foo", None, 1, 2.0])
result = ser.str.repeat(3)
expected = Series(
    ["aaa", np.nan, "bbb", np.nan, np.nan, "foofoofoo", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)
