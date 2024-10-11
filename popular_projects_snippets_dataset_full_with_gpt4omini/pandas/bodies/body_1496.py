# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#40480
df = DataFrame(index=[3, 5, 4], columns=["A", "B"], dtype=float)
df["B"] = "string"
df.loc[[4, 3, 5], "A"] = np.array([1, 2, 3], dtype="int64")
ser = Series([2, 3, 1], index=[3, 5, 4], dtype="int64")
# pre-2.0 this setting swapped in a new array, now it is inplace
#  consistent with non-split-path
expected = DataFrame({"A": ser.astype(float)})
expected["B"] = "string"
tm.assert_frame_equal(df, expected)
