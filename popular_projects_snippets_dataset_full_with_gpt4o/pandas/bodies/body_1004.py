# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_sorted.py
arrays = [
    ["bar", "bar", "baz", "baz", "qux", "qux", "foo", "foo"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
s = Series(np.random.randn(8), index=index)

arrays = [np.array(x) for x in zip(*index.values)]

result = s["qux"]
result2 = s.loc["qux"]
expected = s[arrays[0] == "qux"]
expected.index = expected.index.droplevel(0)
tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)
