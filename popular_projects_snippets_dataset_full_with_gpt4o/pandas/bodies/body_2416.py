# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(np.random.randn(3, 2))
rs = df.loc[df.index == 0, :]
xp = df.reindex([0])
tm.assert_frame_equal(rs, xp)

# GH#1321
df = DataFrame(np.random.randn(3, 2))
rs = df.loc[df.index == 0, df.columns == 1]
xp = df.reindex(index=[0], columns=[1])
tm.assert_frame_equal(rs, xp)
