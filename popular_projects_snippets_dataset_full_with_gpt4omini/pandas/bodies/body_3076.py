# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_copy.py
# GH#31784 _item_cache not cleared on copy causes incorrect reads after updates
df = DataFrame({"a": [1]})

df["x"] = [0]
df["a"]

df.copy()

df["a"].values[0] = -1

tm.assert_frame_equal(df, DataFrame({"a": [-1], "x": [0]}))

df["y"] = [0]

assert df["a"].values[0] == -1
tm.assert_frame_equal(df, DataFrame({"a": [-1], "x": [0], "y": [0]}))
