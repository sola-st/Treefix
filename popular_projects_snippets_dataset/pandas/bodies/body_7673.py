# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH27292
a = Series([1, 2, 3], name="foo")
b = Series(["a", "b", "c"], name="bar")

result = MultiIndex.from_arrays([a, b], names=None)
expected = MultiIndex(
    levels=[[1, 2, 3], ["a", "b", "c"]], codes=[[0, 1, 2], [0, 1, 2]], names=None
)

tm.assert_index_equal(result, expected)
