# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 27614
df = DataFrame(
    np.arange(12).reshape(3, 4), index=[0, 1, 0], columns=[10, 20, 10, 20]
)
df.index.name = "y"
df.columns.name = "x"

results = df.groupby(group_name, axis=1).sum()
expected = df.T.groupby(group_name).sum().T
tm.assert_frame_equal(results, expected)

# test on MI column
iterables = [["bar", "baz", "foo"], ["one", "two"]]
mi = MultiIndex.from_product(iterables=iterables, names=["x", "x1"])
df = DataFrame(np.arange(18).reshape(3, 6), index=[0, 1, 0], columns=mi)
results = df.groupby(group_name, axis=1).sum()
expected = df.T.groupby(group_name).sum().T
tm.assert_frame_equal(results, expected)
