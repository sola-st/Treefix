# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#45135, analogue to GH#44181 for Period don't raise on no-op
# For td64/dt64/dt64tz we already don't raise, but also are
#  checking that we don't unnecessarily upcast to object.
ser = Series(np.arange(3) * 10**9, dtype=np.int64).view(dtype)
df = ser.to_frame()
mask = np.array([False, False, False])

res = ser.where(~mask, "foo")
tm.assert_series_equal(res, ser)

mask2 = mask.reshape(-1, 1)
res2 = df.where(~mask2, "foo")
tm.assert_frame_equal(res2, df)

res3 = ser.mask(mask, "foo")
tm.assert_series_equal(res3, ser)

res4 = df.mask(mask2, "foo")
tm.assert_frame_equal(res4, df)

# opposite case where we are replacing *all* values -> we downcast
#  from object dtype # GH#45768
res5 = df.where(mask2, 4)
expected = DataFrame(4, index=df.index, columns=df.columns)
tm.assert_frame_equal(res5, expected)

# unlike where, Block.putmask does not downcast
df.mask(~mask2, 4, inplace=True)
tm.assert_frame_equal(df, expected.astype(object))
