# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#6254 setting issue
df = DataFrame(index=[3, 5, 4], columns=["A"], dtype=float)
df.loc[[4, 3, 5], "A"] = np.array([1, 2, 3], dtype="int64")

# setting integer values into a float dataframe with loc is inplace,
#  so we retain float dtype
ser = Series([2, 3, 1], index=[3, 5, 4], dtype=float)
expected = DataFrame({"A": ser})
tm.assert_frame_equal(df, expected)
