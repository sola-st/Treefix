# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# Check that -1 / -0.0 returns np.inf, not -np.inf
if numeric_idx.dtype == np.uint64:
    exit()
idx = numeric_idx - 3

expected = Index([-np.inf, -np.inf, -np.inf, np.nan, np.inf], dtype=np.float64)
expected = adjust_negative_zero(zero, expected)

result = op(idx, zero)
tm.assert_index_equal(result, expected)
