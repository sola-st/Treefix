# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
window, min_periods = rolling_consistency_cases

var_x = all_data.rolling(window=window, min_periods=min_periods, center=center).var(
    ddof=ddof
)
assert not (var_x < 0).any().any()

std_x = all_data.rolling(window=window, min_periods=min_periods, center=center).std(
    ddof=ddof
)
assert not (std_x < 0).any().any()

# check that var(x) == std(x)^2
tm.assert_equal(var_x, std_x * std_x)

cov_x_x = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).cov(all_data, ddof=ddof)
assert not (cov_x_x < 0).any().any()

# check that var(x) == cov(x, x)
tm.assert_equal(var_x, cov_x_x)
