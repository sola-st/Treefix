# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
# GH#3217
df = DataFrame({"a": [1, 3], "b": [np.nan, 2]})
df["c"] = np.nan
if using_copy_on_write:
    df.update({"c": Series(["foo"], index=[0])})
else:
    df["c"].update(Series(["foo"], index=[0]))

expected = DataFrame({"a": [1, 3], "b": [np.nan, 2], "c": ["foo", np.nan]})
tm.assert_frame_equal(df, expected)
