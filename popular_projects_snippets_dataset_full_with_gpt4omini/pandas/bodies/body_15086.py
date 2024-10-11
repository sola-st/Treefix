# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
ser = Series(arr)
result = ser.array
expected = PandasArray(arr)
tm.assert_extension_array_equal(result, expected)
