# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
arrays = [
    ["a", "top", "top", "routine1", "routine1", "routine2"],
    ["", "OD", "OD", "result1", "result2", "result1"],
    ["", "wx", "wy", "", "", ""],
]

tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.randn(4, 6), columns=index)

result = df["a"]
expected = df["a", "", ""].rename("a")
tm.assert_series_equal(result, expected)

result = df["routine1", "result1"]
expected = df["routine1", "result1", ""]
expected = expected.rename(("routine1", "result1"))
tm.assert_series_equal(result, expected)
