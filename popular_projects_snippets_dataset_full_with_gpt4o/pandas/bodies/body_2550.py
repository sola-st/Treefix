# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#29334
df = DataFrame([[1, 2], [3, 4], [5, 6]], columns=["A", "B"])
df[columns] = box
tm.assert_frame_equal(df, expected)
