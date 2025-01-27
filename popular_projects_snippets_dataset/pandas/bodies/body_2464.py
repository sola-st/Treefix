# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#49521
df = DataFrame([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
indexer = Series([0, 1], dtype="Int64")
row_indexer = Series([1], dtype="Int64")
result = df.iloc[row_indexer, indexer]
expected = DataFrame([[5, 6]], index=[1])
tm.assert_frame_equal(result, expected)

result = df.iloc[row_indexer.values, indexer.values]
tm.assert_frame_equal(result, expected)
