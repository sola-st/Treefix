# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
value = Series(["-cat", "-1", "+dog"])
expected = Series(["-0cat", "-0001", "+0dog"])
tm.assert_series_equal(value.str.zfill(5), expected)
