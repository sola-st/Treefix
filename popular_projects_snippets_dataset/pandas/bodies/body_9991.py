# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_expanding.py
var_x = all_data.expanding(min_periods=min_periods).var(ddof=ddof)
assert not (var_x < 0).any().any()

if ddof == 0:
    # check that biased var(x) == mean(x^2) - mean(x)^2
    mean_x2 = (all_data * all_data).expanding(min_periods=min_periods).mean()
    mean_x = all_data.expanding(min_periods=min_periods).mean()
    tm.assert_equal(var_x, mean_x2 - (mean_x * mean_x))
