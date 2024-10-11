# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["a", "b", "a\xe4"], dtype=any_string_dtype).str.encode("utf-8")
result = ser.str.decode("utf-8")
expected = ser.map(lambda x: x.decode("utf-8"))
tm.assert_series_equal(result, expected)
