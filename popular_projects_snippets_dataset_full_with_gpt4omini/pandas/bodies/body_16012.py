# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH#42405
ser = Series(data, dtype=dtype)

result = ser.isin(values)
expected = Series(expected, dtype="boolean")

tm.assert_series_equal(result, expected)
