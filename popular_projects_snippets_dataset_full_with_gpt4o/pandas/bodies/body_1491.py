# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# empty (essentially noops)
# before the enforcement of #45333 in 2.0, the loc.setitem here would
#  change the dtype of df.x to int64
expected = DataFrame(columns=["x", "y"])
df = DataFrame(columns=["x", "y"])
with tm.assert_produces_warning(None):
    df.loc[:, "x"] = 1
tm.assert_frame_equal(df, expected)

# setting with setitem swaps in a new array, so changes the dtype
df = DataFrame(columns=["x", "y"])
df["x"] = 1
expected["x"] = expected["x"].astype(np.int64)
tm.assert_frame_equal(df, expected)
