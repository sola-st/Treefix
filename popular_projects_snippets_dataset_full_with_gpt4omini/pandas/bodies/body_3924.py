# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 36113
levels = [np.array([], dtype=np.int64), np.array([], dtype=np.int64)]
expected = Series(dtype=np.float64, index=MultiIndex(levels=levels, codes=[[], []]))
result = DataFrame(dtype=np.float64).stack(dropna=dropna)
tm.assert_series_equal(result, expected)
