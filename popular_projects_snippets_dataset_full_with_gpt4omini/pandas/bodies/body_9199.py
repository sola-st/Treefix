# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# make sure we have correct itemsize on resulting codes
cat = Categorical(["A", "B"])
idx = Index([0.0, 0.5])
result = cat[:0]._quantile(idx, interpolation="linear")
assert result._codes.dtype == np.int8

expected = cat.take([-1, -1], allow_fill=True)
tm.assert_extension_array_equal(result, expected)
