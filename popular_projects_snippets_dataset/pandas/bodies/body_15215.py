# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_mask.py
s = Series(np.random.randn(5))
cond = s > 0

rs = s.copy()
rs.mask(cond, inplace=True)
tm.assert_series_equal(rs.dropna(), s[~cond])
tm.assert_series_equal(rs, s.mask(cond))

rs = s.copy()
rs.mask(cond, -s, inplace=True)
tm.assert_series_equal(rs, s.mask(cond, -s))
