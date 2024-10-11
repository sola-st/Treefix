# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 3561, dups not in selected order
df = DataFrame(
    {"test": [5, 7, 9, 11], "test1": [4.0, 5, 6, 7], "other": list("abcd")},
    index=["A", "A", "B", "C"],
)
rows = ["C", "B"]
expected = DataFrame(
    {"test": [11, 9], "test1": [7.0, 6], "other": ["d", "c"]}, index=rows
)
result = df.loc[rows]
tm.assert_frame_equal(result, expected)

result = df.loc[Index(rows)]
tm.assert_frame_equal(result, expected)

rows = ["C", "B", "E"]
with pytest.raises(KeyError, match="not in index"):
    df.loc[rows]

# see GH5553, make sure we use the right indexer
rows = ["F", "G", "H", "C", "B", "E"]
with pytest.raises(KeyError, match="not in index"):
    df.loc[rows]
