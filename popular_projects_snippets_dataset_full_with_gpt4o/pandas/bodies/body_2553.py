# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
indexer = (x for x in [1, 2])
df.iloc[indexer, 1] = 1
expected = DataFrame({"a": [1, 2, 3], "b": [4, 1, 1]})
tm.assert_frame_equal(df, expected)
