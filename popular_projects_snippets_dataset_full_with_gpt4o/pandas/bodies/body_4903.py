# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series(["fooBAD__barBAD", np.nan, "foo", "BAD"], dtype=any_string_dtype)
result = ser.str.findall("BAD[_]*")
expected = Series([["BAD__", "BAD"], np.nan, [], ["BAD"]])
tm.assert_series_equal(result, expected)
