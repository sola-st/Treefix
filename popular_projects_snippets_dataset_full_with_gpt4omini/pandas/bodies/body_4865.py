# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
ser = Series(["a", "ab", np.nan, "abc"], dtype=any_string_dtype)
result = ser.str.get(2)
expected = Series([np.nan, np.nan, np.nan, "c"], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
