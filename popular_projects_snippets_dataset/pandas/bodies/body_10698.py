# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
# case where groupby axis is 0 and axis keyword in transform is 1

# df has mixed dtype -> multiple blocks
df = DataFrame(
    {0: [1, 3, 5, 7], 1: [2, 4, 6, 8], 2: [1.5, 3.5, 5.5, 7.5]},
    index=["a", "a", "b", "b"],
)
gb = df.groupby(level=0, axis=0)

cmax = gb.cummax(axis=1)
expected = df[[0, 1]].astype(np.float64)
expected[2] = expected[1]
tm.assert_frame_equal(cmax, expected)
