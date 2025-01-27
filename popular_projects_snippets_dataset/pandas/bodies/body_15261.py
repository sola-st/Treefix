# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
s = Series(np.random.randn(10))

np.fix(s)

result = s[...]
tm.assert_series_equal(result, s)

s[...] = 5
assert (result == 5).all()
