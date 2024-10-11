# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# Series
# list/tuple
data = np.random.randn(5, 3)
df = DataFrame(data)
idx_ser = box(np.random.randn(5))
col_ser = box(np.random.randn(3))

idx_eq = df.eq(idx_ser, axis=0)
col_eq = df.eq(col_ser)
idx_ne = df.ne(idx_ser, axis=0)
col_ne = df.ne(col_ser)
tm.assert_frame_equal(col_eq, df == Series(col_ser))
tm.assert_frame_equal(col_eq, -col_ne)
tm.assert_frame_equal(idx_eq, -idx_ne)
tm.assert_frame_equal(idx_eq, df.T.eq(idx_ser).T)
tm.assert_frame_equal(col_eq, df.eq(list(col_ser)))
tm.assert_frame_equal(idx_eq, df.eq(Series(idx_ser), axis=0))
tm.assert_frame_equal(idx_eq, df.eq(list(idx_ser), axis=0))

idx_gt = df.gt(idx_ser, axis=0)
col_gt = df.gt(col_ser)
idx_le = df.le(idx_ser, axis=0)
col_le = df.le(col_ser)

tm.assert_frame_equal(col_gt, df > Series(col_ser))
tm.assert_frame_equal(col_gt, -col_le)
tm.assert_frame_equal(idx_gt, -idx_le)
tm.assert_frame_equal(idx_gt, df.T.gt(idx_ser).T)

idx_ge = df.ge(idx_ser, axis=0)
col_ge = df.ge(col_ser)
idx_lt = df.lt(idx_ser, axis=0)
col_lt = df.lt(col_ser)
tm.assert_frame_equal(col_ge, df >= Series(col_ser))
tm.assert_frame_equal(col_ge, -col_lt)
tm.assert_frame_equal(idx_ge, -idx_lt)
tm.assert_frame_equal(idx_ge, df.T.ge(idx_ser).T)

idx_ser = Series(np.random.randn(5))
col_ser = Series(np.random.randn(3))
