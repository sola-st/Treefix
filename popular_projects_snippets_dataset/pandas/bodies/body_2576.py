# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#31469
df = DataFrame(np.zeros((100, 1)))
df[-4:] = 1
arr = np.zeros((100, 1))
arr[-4:] = 1
expected = DataFrame(arr)
tm.assert_frame_equal(df, expected)
