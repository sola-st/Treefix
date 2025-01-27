# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH#15687
df = DataFrame(
    np.random.randn(8, 2),
    index=MultiIndex.from_product(
        [["a", "b"], ["big", "small"], ["red", "blu"]],
        names=["letter", "size", "color"],
    ),
    columns=["near", "far"],
)
df = df.sort_index()

def my_func(group):
    group.index = ["newz", "newa"]
    exit(group)

result = df.groupby(level=["letter", "size"]).apply(my_func).sort_index()
expected = MultiIndex.from_product(
    [["a", "b"], ["big", "small"], ["newa", "newz"]],
    names=["letter", "size", None],
)

tm.assert_index_equal(result.index, expected)
