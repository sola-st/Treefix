# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH27292
result = MultiIndex.from_product([a, b])
expected = MultiIndex(
    levels=[[1, 2, 3], ["a", "b"]],
    codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
    names=expected_names,
)
tm.assert_index_equal(result, expected)
