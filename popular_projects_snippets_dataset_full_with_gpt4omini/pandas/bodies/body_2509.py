# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#45316
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "a", "b"])
df_orig = df.copy()
view = df["b"]
view.loc[:] = 100
if using_copy_on_write:
    expected = df_orig
else:
    expected = DataFrame([[1, 2, 100], [4, 5, 100]], columns=["a", "a", "b"])
tm.assert_frame_equal(df, expected)
