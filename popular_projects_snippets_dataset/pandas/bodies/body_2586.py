# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39931
df = DataFrame({"a": [1, 4, 2, 3], "b": [5, 6, 7, 8]})
expected = df.copy()
mask = df["a"] >= 3
indexer(df)[mask] = indexer(df)[mask].sort_values("a")
tm.assert_frame_equal(df, expected)
