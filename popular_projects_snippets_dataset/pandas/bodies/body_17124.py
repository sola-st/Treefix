# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
df = DataFrame(
    {"rows": ["a", "b", "c"], "cols": ["x", "y", "z"], "values": [1, 2, 3]}
)
rs = df.pivot_table(columns="cols", aggfunc=np.sum)
xp = df.pivot_table(index="cols", aggfunc=np.sum).T
tm.assert_frame_equal(rs, xp)

rs = df.pivot_table(columns="cols", aggfunc={"values": "mean"})
xp = df.pivot_table(index="cols", aggfunc={"values": "mean"}).T
tm.assert_frame_equal(rs, xp)
