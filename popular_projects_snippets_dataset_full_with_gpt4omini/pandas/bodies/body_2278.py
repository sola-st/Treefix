# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
# see GH#21891
df = DataFrame([1, 2])
res = df.mask([[True], [False]])

exp = DataFrame([np.nan, 2])
tm.assert_frame_equal(res, exp)
