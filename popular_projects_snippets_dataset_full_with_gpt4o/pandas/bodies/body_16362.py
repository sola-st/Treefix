# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 16804
expected = Series([0, 1, 2, 3, 4], dtype=dtype or "int64")
result = Series(range(5), dtype=dtype)
tm.assert_series_equal(result, expected)
