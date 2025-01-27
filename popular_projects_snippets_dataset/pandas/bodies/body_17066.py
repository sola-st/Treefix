# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GH13542
# when multi-index levels are RangeIndex objects
# there is a bug in concat with objects of len 1

df = DataFrame(np.random.randn(9, 2))
df.index = MultiIndex(
    levels=[pd.RangeIndex(3), pd.RangeIndex(3)],
    codes=[np.repeat(np.arange(3), 3), np.tile(np.arange(3), 3)],
)

res = concat([df.iloc[[2, 3, 4], :], df.iloc[[5], :]])
exp = df.iloc[[2, 3, 4, 5], :]
tm.assert_frame_equal(res, exp)
