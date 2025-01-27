# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx

exleft = Index([np.nan, np.inf, np.inf, np.inf, np.inf], dtype=np.float64)
exright = Index([np.nan, np.nan, np.nan, np.nan, np.nan], dtype=np.float64)
exleft = adjust_negative_zero(zero, exleft)

result = divmod(idx, zero)
tm.assert_index_equal(result[0], exleft)
tm.assert_index_equal(result[1], exright)
