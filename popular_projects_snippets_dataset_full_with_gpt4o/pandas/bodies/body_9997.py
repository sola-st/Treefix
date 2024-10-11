# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_expanding.py
# check variance debiasing factors
var_unbiased_x = all_data.expanding(min_periods=min_periods).var()
var_biased_x = all_data.expanding(min_periods=min_periods).var(ddof=0)
var_debiasing_factors_x = all_data.expanding().count() / (
    all_data.expanding().count() - 1.0
).replace(0.0, np.nan)
tm.assert_equal(var_unbiased_x, var_biased_x * var_debiasing_factors_x)
