# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
arrays = [
    ["a", "top", "top", "routine1", "routine1", "routine2"],
    ["", "OD", "OD", "result1", "result2", "result1"],
    ["", "wx", "wy", "", "", ""],
]

tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.randn(4, 6), columns=index)

result = df.copy()
expected = df.copy()
result["b"] = [1, 2, 3, 4]
expected["b", "", ""] = [1, 2, 3, 4]
tm.assert_frame_equal(result, expected)
