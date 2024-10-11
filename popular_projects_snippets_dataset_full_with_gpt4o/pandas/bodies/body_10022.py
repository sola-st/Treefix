# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
com = 3.0
count_x = consistent_data.expanding(min_periods=min_periods).count()
var_x = consistent_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).var(bias=bias)

# check that variance of constant series is identically 0
assert not (var_x > 0).any().any()
expected = consistent_data * np.nan
expected[count_x >= max(min_periods, 1)] = 0.0
if not bias:
    expected[count_x < 2] = np.nan
tm.assert_equal(var_x, expected)
