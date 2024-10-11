# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
rng5 = np.arange(5, dtype="float64")

result = idx * Series(rng5 + 0.1)
expected = Series(rng5 * (rng5 + 0.1))
tm.assert_series_equal(result, expected)
