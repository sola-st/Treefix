# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_expanding.py
count_x = consistent_data.expanding(min_periods=min_periods).count()
var_x = consistent_data.expanding(min_periods=min_periods).var(ddof=ddof)

# check that variance of constant series is identically 0
assert not (var_x > 0).any().any()
expected = consistent_data * np.nan
expected[count_x >= max(min_periods, 1)] = 0.0
if ddof == 1:
    expected[count_x < 2] = np.nan
tm.assert_equal(var_x, expected)
