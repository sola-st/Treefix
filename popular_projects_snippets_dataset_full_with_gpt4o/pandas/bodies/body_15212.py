# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_mask.py
# compare with tested results in test_where
s = Series(np.random.randn(5))
cond = s > 0

rs = s.where(~cond, np.nan)
tm.assert_series_equal(rs, s.mask(cond))

rs = s.where(~cond)
rs2 = s.mask(cond)
tm.assert_series_equal(rs, rs2)

rs = s.where(~cond, -s)
rs2 = s.mask(cond, -s)
tm.assert_series_equal(rs, rs2)

cond = Series([True, False, False, True, False], index=s.index)
s2 = -(s.abs())
rs = s2.where(~cond[:3])
rs2 = s2.mask(cond[:3])
tm.assert_series_equal(rs, rs2)

rs = s2.where(~cond[:3], -s2)
rs2 = s2.mask(cond[:3], -s2)
tm.assert_series_equal(rs, rs2)

msg = "Array conditional must be same shape as self"
with pytest.raises(ValueError, match=msg):
    s.mask(1)
with pytest.raises(ValueError, match=msg):
    s.mask(cond[:3].values, -s)
