# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 7972
n = 6
x = np.arange(n)
df = DataFrame({"a": x // 2, "b": 2.0 * x, "c": 3.0 * x})
df2 = DataFrame({"a": x // 2 * 1.0, "b": 2.0 * x, "c": 3.0 * x})

gb = df.groupby("a")
result = gb.transform("mean")

gb2 = df2.groupby("a")
expected = gb2.transform("mean")
tm.assert_frame_equal(result, expected)
