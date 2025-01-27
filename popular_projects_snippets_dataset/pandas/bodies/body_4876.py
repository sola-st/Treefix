# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series(["fooBAD__barBAD", np.nan], dtype=any_string_dtype)

result = ser.str.replace("BAD[_]*", "", regex=True)
expected = Series(["foobar", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
