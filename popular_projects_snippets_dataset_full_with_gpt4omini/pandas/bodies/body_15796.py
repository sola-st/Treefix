# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# https://github.com/pandas-dev/pandas/issues/36904
ser = Series(["a", "b", value], dtype=object)
result = ser.astype(str)
expected = Series(["a", "b", string_value], dtype=object)
tm.assert_series_equal(result, expected)
