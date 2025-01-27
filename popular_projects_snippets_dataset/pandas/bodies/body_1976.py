# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = Series(["1", "-3.14", last_val])
result = to_numeric(ser)

expected = Series([1, -3.14, 7])
tm.assert_series_equal(result, expected)
