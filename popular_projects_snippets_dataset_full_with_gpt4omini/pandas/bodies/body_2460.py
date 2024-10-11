# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#48124
df = DataFrame(
    index=MultiIndex.from_product(
        [["A", "B"], ["a", "b", "c"]], names=["first", "second"]
    )
)
indexer_tuple = namedtuple("Indexer", df.index.names)
idxr = indexer_tuple(first="A", second=["a", "b"])
result = df.loc[idxr, :]
expected = DataFrame(
    index=MultiIndex.from_tuples(
        [("A", "a"), ("A", "b")], names=["first", "second"]
    )
)
tm.assert_frame_equal(result, expected)
