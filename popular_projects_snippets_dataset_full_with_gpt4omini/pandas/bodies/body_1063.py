# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
# GH 4145
df = dataframe_with_duplicate_index
index = Index(["h1", "h3", "h5"])
columns = MultiIndex.from_tuples([("A", "A1")], names=["main", "sub"])
expected = DataFrame([["a", 1, 1]], index=columns, columns=index).T

result = indexer(df)
tm.assert_frame_equal(result, expected)
