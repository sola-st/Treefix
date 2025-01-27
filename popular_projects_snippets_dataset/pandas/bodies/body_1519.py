# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# only appends one value
expected = DataFrame({"x": [1.0], "y": [np.nan]})
df = DataFrame(columns=["x", "y"], dtype=float)
df.loc[0, "x"] = expected.loc[0, "x"]
tm.assert_frame_equal(df, expected)
