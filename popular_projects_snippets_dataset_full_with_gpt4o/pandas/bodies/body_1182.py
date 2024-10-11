# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
df_orig = DataFrame(
    np.arange(6).reshape(3, 2), columns=["A", "B"], dtype="int64"
)

# iloc/iat raise
df = df_orig.copy()

msg = "iloc cannot enlarge its target object"
with pytest.raises(IndexError, match=msg):
    df.iloc[4, 2] = 5.0

msg = "index 2 is out of bounds for axis 0 with size 2"
if using_array_manager:
    msg = "list index out of range"
with pytest.raises(IndexError, match=msg):
    df.iat[4, 2] = 5.0

# row setting where it exists
expected = DataFrame(dict({"A": [0, 4, 4], "B": [1, 5, 5]}))
df = df_orig.copy()
df.iloc[1] = df.iloc[2]
tm.assert_frame_equal(df, expected)

expected = DataFrame(dict({"A": [0, 4, 4], "B": [1, 5, 5]}))
df = df_orig.copy()
df.loc[1] = df.loc[2]
tm.assert_frame_equal(df, expected)

# like 2578, partial setting with dtype preservation
expected = DataFrame(dict({"A": [0, 2, 4, 4], "B": [1, 3, 5, 5]}))
df = df_orig.copy()
df.loc[3] = df.loc[2]
tm.assert_frame_equal(df, expected)

# single dtype frame, overwrite
expected = DataFrame(dict({"A": [0, 2, 4], "B": [0, 2, 4]}))
df = df_orig.copy()
df.loc[:, "B"] = df.loc[:, "A"]
tm.assert_frame_equal(df, expected)

# mixed dtype frame, overwrite
expected = DataFrame(dict({"A": [0, 2, 4], "B": Series([0.0, 2.0, 4.0])}))
df = df_orig.copy()
df["B"] = df["B"].astype(np.float64)
# as of 2.0, df.loc[:, "B"] = ... attempts (and here succeeds) at
#  setting inplace
df.loc[:, "B"] = df.loc[:, "A"]
tm.assert_frame_equal(df, expected)

# single dtype frame, partial setting
expected = df_orig.copy()
expected["C"] = df["A"]
df = df_orig.copy()
df.loc[:, "C"] = df.loc[:, "A"]
tm.assert_frame_equal(df, expected)

# mixed frame, partial setting
expected = df_orig.copy()
expected["C"] = df["A"]
df = df_orig.copy()
df.loc[:, "C"] = df.loc[:, "A"]
tm.assert_frame_equal(df, expected)
