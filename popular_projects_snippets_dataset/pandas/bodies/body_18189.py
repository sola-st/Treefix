# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx

expected = Index([np.nan, np.inf, np.inf, np.inf, np.inf], dtype=np.float64)
# We only adjust for Index, because Series does not yet apply
#  the adjustment correctly.
expected2 = adjust_negative_zero(zero, expected)

result = idx // zero
tm.assert_index_equal(result, expected2)
ser_compat = Series(idx).astype("i8") // np.array(zero).astype("i8")
tm.assert_series_equal(ser_compat, Series(expected))
