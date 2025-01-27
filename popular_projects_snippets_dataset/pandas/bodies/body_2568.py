# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#39010
df = DataFrame([[1, 2], [3, 4]])
df["0 - Name"] = [5, 6]
expected = DataFrame([[1, 2, 5], [3, 4, 6]], columns=[0, 1, "0 - Name"])
tm.assert_frame_equal(df, expected)
