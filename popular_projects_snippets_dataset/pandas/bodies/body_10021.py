# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
com = 3.0

mean_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).mean()
var_x = all_data.ewm(
    com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na
).var(bias=bias)
assert not (var_x < 0).any().any()

if bias:
    # check that biased var(x) == mean(x^2) - mean(x)^2
    mean_x2 = (
        (all_data * all_data)
        .ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na)
        .mean()
    )
    tm.assert_equal(var_x, mean_x2 - (mean_x * mean_x))
