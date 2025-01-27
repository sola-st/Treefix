# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
# see gh-9743
s = Series(np.arange(10), dtype=dtype)
values = [2.5, 3.5, 4.5, 5.5, 6.5]
mask = s < 5
expected = Series(values + list(range(5, 10)), dtype=expected_dtype)
s[mask] = values
tm.assert_series_equal(s, expected)
