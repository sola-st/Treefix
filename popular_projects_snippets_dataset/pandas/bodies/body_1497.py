# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#40480
df = DataFrame(index=[1, 2, 3], columns=["A", "B"], dtype=float)
df["B"] = "string"
df.loc[slice(3, 0, -1), "A"] = np.array([1, 2, 3], dtype="int64")
# pre-2.0 this setting swapped in a new array, now it is inplace
#  consistent with non-split-path
expected = DataFrame({"A": [3.0, 2.0, 1.0], "B": "string"}, index=[1, 2, 3])
tm.assert_frame_equal(df, expected)
