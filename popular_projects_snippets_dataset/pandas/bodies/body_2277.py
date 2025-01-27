# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
df = DataFrame(np.random.randn(5, 3))
cond = df > 0

rs = df.where(cond, np.nan)
tm.assert_frame_equal(rs, df.mask(df <= 0))
tm.assert_frame_equal(rs, df.mask(~cond))

other = DataFrame(np.random.randn(5, 3))
rs = df.where(cond, other)
tm.assert_frame_equal(rs, df.mask(df <= 0, other))
tm.assert_frame_equal(rs, df.mask(~cond, other))
