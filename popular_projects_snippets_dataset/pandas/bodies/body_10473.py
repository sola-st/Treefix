# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
# GH12768
df = DataFrame({"a": [1, 1, 2], "b": [1, 2, 0]})
res = df.groupby("a")
res = res.filter(lambda x: x["b"].sum() > 5, dropna=False)
expected = DataFrame({"a": [np.nan] * 3, "b": [np.nan] * 3})
tm.assert_frame_equal(expected, res)

df = DataFrame({"a": [1, 1, 2], "b": [1, 2, 0]})
res = df.groupby("a")
res = res.filter(lambda x: x["b"].sum() > 5, dropna=True)
expected = DataFrame({"a": [], "b": []}, dtype="int64")
tm.assert_frame_equal(expected, res)
