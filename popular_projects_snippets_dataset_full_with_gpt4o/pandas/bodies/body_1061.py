# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
# Slicing MultiIndex including levels with nan values, for more information
# see GH#25154
df = DataFrame(
    [[1, 2, 3], [4, 5, 6]],
    columns=MultiIndex.from_tuples(
        [("a", "foo"), ("b", "bar"), ("b", nulls_fixture)]
    ),
    dtype="int64",
)

result = df.loc[:, indexer]
tm.assert_equal(result, expected)
