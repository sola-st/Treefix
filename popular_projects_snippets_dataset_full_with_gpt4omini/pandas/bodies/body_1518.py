# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#37932 same as test_loc_setitem_empty_append_expands_rows
#  but with mixed dtype so we go through take_split_path
data = [1, 2, 3]
expected = DataFrame({"x": data, "y": [None] * len(data)})

df = DataFrame(columns=["x", "y"])
df["x"] = df["x"].astype(np.int64)
df.loc[:, "x"] = data
tm.assert_frame_equal(df, expected)
