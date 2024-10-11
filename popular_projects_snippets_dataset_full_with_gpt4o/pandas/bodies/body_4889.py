# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# GH16808 literal replace (regex=False vs regex=True)
ser = Series(["f.o", "foo", np.nan], dtype=any_string_dtype)
expected = Series(expected, dtype=any_string_dtype)
result = ser.str.replace("f.", "ba", regex=regex)
tm.assert_series_equal(result, expected)
