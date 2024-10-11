# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#15166
df = DataFrame(
    data=np.arange(2, 22, 2),
    index=MultiIndex(
        levels=[CategoricalIndex(["a", "b"]), range(10)],
        codes=[[0] * 5 + [1] * 5, range(10)],
        names=["Index1", "Index2"],
    ),
)

expected = CategoricalIndex(
    ["a", "b"],
    categories=["a", "b"],
    ordered=False,
    name="Index1",
    dtype="category",
)

result = df.index.levels[0]
tm.assert_index_equal(result, expected)

result = df.loc[["a"]].index.levels[0]
tm.assert_index_equal(result, expected)
