# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# this refers to GH 32904
df = DataFrame(np.random.random((10, 3)) * 100, columns=["a", "b", "c"])

ax = df.plot.scatter(x="a", y="b", s="c")
tm.assert_numpy_array_equal(df["c"].values, right=ax.collections[0].get_sizes())
