# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#34034
df = DataFrame(
    [[20, "a"], [200, "a"], [200, "a"]],
    columns=["col1", "col2"],
    index=[10, 1, 1],
)
df.loc[1, "col1"] = np.arange(2)
expected = DataFrame(
    [[20, "a"], [0, "a"], [1, "a"]], columns=["col1", "col2"], index=[10, 1, 1]
)
tm.assert_frame_equal(df, expected)
