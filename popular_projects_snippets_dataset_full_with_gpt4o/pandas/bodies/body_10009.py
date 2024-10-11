# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
window, min_periods = rolling_consistency_cases

var_x = all_data.rolling(window=window, min_periods=min_periods, center=center).var(
    ddof=ddof
)
assert not (var_x < 0).any().any()

if ddof == 0:
    # check that biased var(x) == mean(x^2) - mean(x)^2
    mean_x = all_data.rolling(
        window=window, min_periods=min_periods, center=center
    ).mean()
    mean_x2 = (
        (all_data * all_data)
        .rolling(window=window, min_periods=min_periods, center=center)
        .mean()
    )
    tm.assert_equal(var_x, mean_x2 - (mean_x * mean_x))
