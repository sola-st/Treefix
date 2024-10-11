# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#38521
df = DataFrame(columns=["a", "b", "b"], dtype="float64")
df.loc[:, "a"] = list(range(2))
expected = DataFrame(
    [[0, np.nan, np.nan], [1, np.nan, np.nan]], columns=["a", "b", "b"]
)
tm.assert_frame_equal(df, expected)
