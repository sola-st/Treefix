# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
index_lists = [["a", "a", "b", "b"], ["x", "y", "x", "y"]]

multi = DataFrame(
    np.random.randn(4, 4),
    index=[np.array(x) for x in index_lists],
)
assert isinstance(multi.index, MultiIndex)
assert not isinstance(multi.columns, MultiIndex)

multi = DataFrame(np.random.randn(4, 4), columns=index_lists)
assert isinstance(multi.columns, MultiIndex)
