# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
window, min_periods = rolling_consistency_cases

# check variance debiasing factors
var_unbiased_x = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).var()
var_biased_x = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).var(ddof=0)
var_debiasing_factors_x = (
    all_data.rolling(window=window, min_periods=min_periods, center=center)
    .count()
    .divide(
        (
            all_data.rolling(
                window=window, min_periods=min_periods, center=center
            ).count()
            - 1.0
        ).replace(0.0, np.nan)
    )
)
tm.assert_equal(var_unbiased_x, var_biased_x * var_debiasing_factors_x)
