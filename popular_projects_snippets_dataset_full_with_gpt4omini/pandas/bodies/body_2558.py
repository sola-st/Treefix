# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#47216
df = DataFrame({"a": [1, 2], "b": [3, 4], **vals})
df.loc[:, "a"] = {1: 100, 0: 200}
df.loc[:, "c"] = {0: 5, 1: 6}
df.loc[:, "e"] = {1: 5}
expected = DataFrame(
    {"a": [200, 100], "b": [3, 4], **vals, "c": [5, 6], "e": [np.nan, 5]}
)
tm.assert_frame_equal(df, expected)
