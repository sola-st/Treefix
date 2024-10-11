# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH4312 (iloc)
df_orig = DataFrame(
    [["1", "2", "3", ".4", 5, 6.0, "foo"]], columns=list("ABCDEFG")
)

df = df_orig.copy()

# with the enforcement of GH#45333 in 2.0, this setting is attempted inplace,
#  so object dtype is retained
df.iloc[:, 0:2] = df.iloc[:, 0:2].astype(np.int64)
expected = DataFrame(
    [[1, 2, "3", ".4", 5, 6.0, "foo"]], columns=list("ABCDEFG")
)
expected["A"] = expected["A"].astype(object)
expected["B"] = expected["B"].astype(object)
tm.assert_frame_equal(df, expected)

# GH5702 (loc)
df = df_orig.copy()
df.loc[:, "A"] = df.loc[:, "A"].astype(np.int64)
expected = DataFrame(
    [[1, "2", "3", ".4", 5, 6.0, "foo"]], columns=list("ABCDEFG")
)
expected["A"] = expected["A"].astype(object)
tm.assert_frame_equal(df, expected)

df = df_orig.copy()
df.loc[:, ["B", "C"]] = df.loc[:, ["B", "C"]].astype(np.int64)
expected = DataFrame(
    [["1", 2, 3, ".4", 5, 6.0, "foo"]], columns=list("ABCDEFG")
)
expected["B"] = expected["B"].astype(object)
expected["C"] = expected["C"].astype(object)
tm.assert_frame_equal(df, expected)
