# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#22046
df1 = DataFrame({"a2": [11, 12, 13], "b2": [14, 15, 16]})
df2 = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
df2.iloc[:, indexer] = df1.iloc[:, [0]]
expected = DataFrame({"a": [1, 2, 3], "b": [11, 12, 13], "c": [7, 8, 9]})
tm.assert_frame_equal(df2, expected)
