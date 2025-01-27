# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
# GH#10665
# same test cases as test_align_multiindex in test_series.py

midx = pd.MultiIndex.from_product(
    [range(2), range(3), range(2)], names=("a", "b", "c")
)
idx = Index(range(2), name="b")
df1 = DataFrame(np.arange(12, dtype="int64"), index=midx)
df2 = DataFrame(np.arange(2, dtype="int64"), index=idx)

# these must be the same results (but flipped)
res1l, res1r = df1.align(df2, join="left")
res2l, res2r = df2.align(df1, join="right")

expl = df1
tm.assert_frame_equal(expl, res1l)
tm.assert_frame_equal(expl, res2r)
expr = DataFrame([0, 0, 1, 1, np.nan, np.nan] * 2, index=midx)
tm.assert_frame_equal(expr, res1r)
tm.assert_frame_equal(expr, res2l)

res1l, res1r = df1.align(df2, join="right")
res2l, res2r = df2.align(df1, join="left")

exp_idx = pd.MultiIndex.from_product(
    [range(2), range(2), range(2)], names=("a", "b", "c")
)
expl = DataFrame([0, 1, 2, 3, 6, 7, 8, 9], index=exp_idx)
tm.assert_frame_equal(expl, res1l)
tm.assert_frame_equal(expl, res2r)
expr = DataFrame([0, 0, 1, 1] * 2, index=exp_idx)
tm.assert_frame_equal(expr, res1r)
tm.assert_frame_equal(expr, res2l)
