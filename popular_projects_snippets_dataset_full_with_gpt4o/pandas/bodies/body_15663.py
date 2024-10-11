# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH26796

s = Series(data)
expected = Series(expected_data)
result = s.interpolate(**kwargs)
tm.assert_series_equal(result, expected)
