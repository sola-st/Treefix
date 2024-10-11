# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
# GH 5528
tup = zip(*[["a", "a", "b", "b"], ["x", "y", "x", "y"]])
index = MultiIndex.from_tuples(tup)
df = DataFrame(np.random.randn(4, 4), index=index)
result = df.iloc[[2, 3]]
expected = df.xs("b", drop_level=False)
tm.assert_frame_equal(result, expected)
