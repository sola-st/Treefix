# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 29334
df = DataFrame([[1, 2], [3, 4], [5, 6]], columns=["A", "B"])

df.loc[index] = box
tm.assert_frame_equal(df, expected)
