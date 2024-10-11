# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pop.py
arrays = [
    ["a", "top", "top", "routine1", "routine1", "routine2"],
    ["", "OD", "OD", "result1", "result2", "result1"],
    ["", "wx", "wy", "", "", ""],
]

tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.randn(4, 6), columns=index)

df1 = df.copy()
df2 = df.copy()
result = df1.pop("a")
expected = df2.pop(("a", "", ""))
tm.assert_series_equal(expected, result, check_names=False)
tm.assert_frame_equal(df1, df2)
assert result.name == "a"

expected = df1["top"]
df1 = df1.drop(["top"], axis=1)
result = df2.pop("top")
tm.assert_frame_equal(expected, result)
tm.assert_frame_equal(df1, df2)
