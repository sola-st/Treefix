# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = Series([1, -3.14, "apple"])
result = to_numeric(ser, errors=errors)

expected = Series(exp_data)
tm.assert_series_equal(result, expected)
