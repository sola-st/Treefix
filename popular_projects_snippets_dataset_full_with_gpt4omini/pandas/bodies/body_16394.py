# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
index_lists = [["a", "a", "b", "b"], ["x", "y", "x", "y"]]

multi = Series(1.0, index=[np.array(x) for x in index_lists])
assert isinstance(multi.index, MultiIndex)

multi = Series(1.0, index=index_lists)
assert isinstance(multi.index, MultiIndex)

multi = Series(range(4), index=index_lists)
assert isinstance(multi.index, MultiIndex)
