# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
s = Series(np.random.randn(5))
cond = s > 0

rs = s.copy()

rs.where(cond, inplace=True)
tm.assert_series_equal(rs.dropna(), s[cond])
tm.assert_series_equal(rs, s.where(cond))

rs = s.copy()
rs.where(cond, -s, inplace=True)
tm.assert_series_equal(rs, s.where(cond, -s))
