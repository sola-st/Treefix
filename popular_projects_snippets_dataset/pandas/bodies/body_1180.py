# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH#6171
# consistency on empty frames
df = DataFrame(columns=["x", "y"])
df["x"] = [1, 2]
expected = DataFrame({"x": [1, 2], "y": [np.nan, np.nan]})
tm.assert_frame_equal(df, expected, check_dtype=False)

df = DataFrame(columns=["x", "y"])
df["x"] = ["1", "2"]
expected = DataFrame({"x": ["1", "2"], "y": [np.nan, np.nan]}, dtype=object)
tm.assert_frame_equal(df, expected)

df = DataFrame(columns=["x", "y"])
df.loc[0, "x"] = 1
expected = DataFrame({"x": [1], "y": [np.nan]})
tm.assert_frame_equal(df, expected, check_dtype=False)
