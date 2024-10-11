# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# list-like must conform
df = DataFrame(columns=["A", "B"])

msg = "cannot set a row with mismatched columns"
with pytest.raises(ValueError, match=msg):
    df.loc[0] = [1, 2, 3]

df = DataFrame(columns=["A", "B"])
df.loc[3] = [6, 7]  # length matches len(df.columns) --> OK!

exp = DataFrame([[6, 7]], index=[3], columns=["A", "B"], dtype=np.int64)
tm.assert_frame_equal(df, exp)
