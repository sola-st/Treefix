# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
com = 3.0
var_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).var(bias=bias)
assert not (var_x < 0).any().any()

std_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).std(bias=bias)
assert not (std_x < 0).any().any()

# check that var(x) == std(x)^2
tm.assert_equal(var_x, std_x * std_x)

cov_x_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).cov(all_data, bias=bias)
assert not (cov_x_x < 0).any().any()

# check that var(x) == cov(x, x)
tm.assert_equal(var_x, cov_x_x)
