# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH 20883

ser = Series(data)
result = ser.isin(is_in)
expected = Series([True, False])

tm.assert_series_equal(result, expected)
