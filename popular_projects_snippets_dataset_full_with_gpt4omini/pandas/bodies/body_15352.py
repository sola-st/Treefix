# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = Series(range(5))
key = (slice(3),)

result = ser[key]
expected = ser[key[0]]
tm.assert_series_equal(result, expected)
