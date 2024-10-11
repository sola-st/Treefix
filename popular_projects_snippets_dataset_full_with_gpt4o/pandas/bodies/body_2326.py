# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#45768
obj = frame_or_series([pd.Interval(0, 0)] * 2)
other = frame_or_series([1.0, 2.0])
res = obj.where(~obj.notna(), other)

# since all entries are being changed, we will downcast result
#  from object to ints (not floats)
tm.assert_equal(res, other.astype(np.int64))

# unlike where, Block.putmask does not downcast
obj.mask(obj.notna(), other, inplace=True)
tm.assert_equal(obj, other.astype(object))
