# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# full replacements / no nans
df = DataFrame({"A": [1.0, 2.0, 3.0, 4.0]})

# With the enforcement of GH#45333 in 2.0, this assignment occurs inplace,
#  so float64 is retained
df.iloc[:, 0] = df["A"].astype(np.int64)
expected = DataFrame({"A": [1.0, 2.0, 3.0, 4.0]})
tm.assert_frame_equal(df, expected)

df = DataFrame({"A": [1.0, 2.0, 3.0, 4.0]})
df.loc[:, "A"] = df["A"].astype(np.int64)
tm.assert_frame_equal(df, expected)
