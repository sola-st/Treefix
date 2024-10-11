# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#40440
df = DataFrame([[1, 3, 5]] + [[2, 4, 6]] * n, columns=["a", "b", "c"])
indexer(df)[1:] = box([10, 11, 12])
expected = DataFrame([[1, 3, 5]] + [[10, 11, 12]] * n, columns=["a", "b", "c"])
tm.assert_frame_equal(df, expected)
