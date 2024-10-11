# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#56
arr = Series(np.random.randn(10), index=np.arange(10), dtype=object)

result = op(1.0, arr)
expected = op(1.0, arr.astype(float))
tm.assert_series_equal(result.astype(float), expected)
