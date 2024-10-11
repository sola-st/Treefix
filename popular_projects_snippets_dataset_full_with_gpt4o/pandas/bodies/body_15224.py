# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
s = Series(np.random.randn(5))
cond = s > 0

rs = s.where(cond).dropna()
rs2 = s[cond]
tm.assert_series_equal(rs, rs2)

rs = s.where(cond, -s)
tm.assert_series_equal(rs, s.abs())

rs = s.where(cond)
assert s.shape == rs.shape
assert rs is not s

# test alignment
cond = Series([True, False, False, True, False], index=s.index)
s2 = -(s.abs())

expected = s2[cond].reindex(s2.index[:3]).reindex(s2.index)
rs = s2.where(cond[:3])
tm.assert_series_equal(rs, expected)

expected = s2.abs()
expected.iloc[0] = s2[0]
rs = s2.where(cond[:3], -s2)
tm.assert_series_equal(rs, expected)
