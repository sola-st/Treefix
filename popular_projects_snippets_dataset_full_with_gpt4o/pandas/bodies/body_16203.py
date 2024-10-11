# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
ser = Series([frozenset([1]), frozenset([1, 2])])

result = ser == frozenset([1])
expected = Series([True, False])
tm.assert_series_equal(result, expected)
