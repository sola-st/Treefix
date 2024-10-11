# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_update.py
result = Series(data, dtype=dtype)
other = Series(other, dtype=dtype)
expected = Series(expected, dtype=dtype)

result.update(other)
tm.assert_series_equal(result, expected)
