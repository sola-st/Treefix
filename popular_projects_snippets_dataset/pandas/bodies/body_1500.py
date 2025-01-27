# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 8669
# invalid coercion of nan -> int
df = DataFrame({"A": [1, 2, 3], "B": np.nan})
df.loc[df.B > df.A, "B"] = df.A
expected = DataFrame({"A": [1, 2, 3], "B": np.nan})
tm.assert_frame_equal(df, expected)
