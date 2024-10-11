# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#15695
cols = ["A", "B", "C"] * 2
df = DataFrame(index=range(3), columns=cols)
df.loc[0, "A"] = (0, 3)
df.loc[:, "B"] = (1, 4)
df["C"] = (2, 5)
expected = DataFrame(
    [
        [0, 1, 2, 3, 4, 5],
        [np.nan, 1, 2, np.nan, 4, 5],
        [np.nan, 1, 2, np.nan, 4, 5],
    ],
    dtype="object",
)

# set these with unique columns to be extra-unambiguous
expected[2] = expected[2].astype(np.int64)
expected[5] = expected[5].astype(np.int64)
expected.columns = cols

tm.assert_frame_equal(df, expected)
