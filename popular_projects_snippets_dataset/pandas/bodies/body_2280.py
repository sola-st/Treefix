# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
# GH#4071
df = DataFrame([[1, 2]])
res = df.mask(DataFrame([[True, False]]))
expec = DataFrame([[np.nan, 2]])
tm.assert_frame_equal(res, expec)
