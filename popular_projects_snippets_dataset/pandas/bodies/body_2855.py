# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#45423
# Two relevant paths:
#  1) not _can_hold_na (e.g. integer)
#  2) _can_hold_na + noop + not can_hold_element

obj = frame_or_series([1, 2, 3], dtype=np.int64)
res = obj.fillna("foo", downcast=np.dtype(np.int32))
expected = obj.astype(np.int32)
tm.assert_equal(res, expected)

obj2 = obj.astype(np.float64)
res2 = obj2.fillna("foo", downcast="infer")
expected2 = obj  # get back int64
tm.assert_equal(res2, expected2)

res3 = obj2.fillna("foo", downcast=np.dtype(np.int32))
tm.assert_equal(res3, expected)
